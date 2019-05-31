<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="ve-picker">
    <div class="selected-date">
      <div class="selected-date-content">
        <span class="week-select">周{{ weeks[startDateMomentWeek] }}</span>
        <span>{{ startDateMomentMonth }}</span>
      </div>
      <span></span>
      <div class="selected-date-content">
        <span class="week-select">周{{ weeks[endDateMomentWeek] }}</span>
        <span>{{ endDateMomentMonth }}</span>
      </div>
    </div>
    <div class="week">
      <ul>
        <li v-for="item in weeks" :key="item">{{ item }}</li>
      </ul>
    </div>
    <div class="select-date-picker" ref="datePicker">
      <div id="month-list" v-bind:state="waiting ? 'waiting' : 'complete' " v-on:scroll="loadRepeat">
        <section class="month-item" v-for="(month, mindex) in monthList" :key="mindex">
          <p class="month-info">{{month.numStr}}月</p>
          <ul class="month-main">
            <li class="item null" v-for="(pmitem, pmindex) in month.prefix" :key="pmindex"></li>
            <li class="item date" v-hammer:tap="() => checkDate(date)" v-for="(date, dindex) in month.dateList" :key="dindex"
                :class="{'disable': date.isDisable,'today': date.isToday,'start-date': date.isStartDate, 'end-date': date.isEndDate, 'progress': date.isProgress}">
              <span class="num">{{date.dateData ? date.dateData.date : ''}}</span>
            </li>
            <li class="item null" v-for="(smitem, smindex) in month.surfix" :key="smindex"></li>
          </ul>
        </section>
      </div>
    </div>
    <button :disabled="disabled" class="primary date-confirm" @click.stop="handleConfirm" :class="{iPhoneX: isX}">确定</button>
  </div>
</template>

<script>
  import moment from 'moment'
  import BScroll from 'better-scroll'
  import browser from '../../utils/browser'

  var TODAY = moment().startOf('date')
  var SCROLL_LIMIT_PERCENT = 0.5
  var MONTH_CH = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']

  var DateItem
  var MonthItem
  var makeDateList = function (data) {
    var firstDateInMonth = data.curMonth.clone()
    var lastDateInMonth = data.curMonth.clone().endOf('month')
    var prefixAmount = firstDateInMonth.day()
    var contentAmount = lastDateInMonth.date()
    var surfixAmount = (6 - lastDateInMonth.day()) % 6
    var result = []
    var i, l

    for (i = 0, l = prefixAmount + contentAmount + surfixAmount; i < l; i += 1) {
      if (i < prefixAmount || i >= prefixAmount + contentAmount) {
        result.push(new DateItem())
      } else {
        result.push(new DateItem(firstDateInMonth.clone(), data.disableBeforeMoment, data.disableAfterMoment))
        firstDateInMonth.add(1, 'd')
      }
    }
    return result
  }
  var formatDate = function (date, format) {
    return moment(date).format(format || 'YYYY-MM-DD')
  }

  DateItem = function (date, disableBeforeMoment, disableAfterMoment) {
    if (date !== undefined) {
      this.dateData = {
        year: date.year(),
        month: date.month(),
        date: date.date()
      }
      this.timeStamp = date.toDate().getTime()
      this.isToday = date.isSame(TODAY)
      this.isDisable = (disableBeforeMoment && date.isBefore(disableBeforeMoment)) || (disableAfterMoment && date.isAfter(disableAfterMoment))
    } else {
      this.isNull = true
    }
    this.isStartDate = false
    this.isEndDate = false
    this.isProgress = false
  }
  MonthItem = function (data) {
    var targetMonth = data.curMonth.clone().startOf('month')
    this.num = targetMonth.month()
    this.numStr = MONTH_CH[this.num]
    this.dateList = makeDateList(data)
  }
  export default {
    name: "datePicker",
    props: {
      labels: {
        type: Array,
        default: () => ['入住','离开']
      },
      isSame: { // 是否能相同
        type: Boolean,
        default: false
      },
      startDate: String,
      endDate: String,
      showAmount: {
        type: Number,
        default: 3
      },
      disableBefore: {
        type: String,
        default: formatDate(TODAY)
      },
      disableAfter: String,
      start: String,
      sameEnable: {
        type: Boolean,
        default: true
      },
      day: {
        type: Number,
        default: 24*60*60*1000
      }
    },
    data() {
      var startMonth = moment(this.start).startOf('month')
      var singleMode = this.labels.length === 1
      return {
        isX: false,
        disabled: true,
        weeks: ['日', '一', '二', '三', '四', '五', '六'],
        disableBeforeMoment: moment(this.disableBefore),
        disableAfterMoment: this.disableAfter && moment(this.disableAfter),
        firstMonth: startMonth,
        curMonth: startMonth.clone(),
        curAmount: 0,
        monthList: [],
        startDateMoment: this.startDate && moment(this.startDate),
        singleMode: singleMode,
        endDateMoment: !singleMode && this.endDate && moment(this.endDate),
        loadFreeze: false,
        animateFreeze: false,
        waiting: false,
      }
    },
    computed: {
      startDateMomentWeek () {
        return this.startDateMoment && this.startDateMoment.day()
      },
      startDateMomentMonth () {
        return this.startDateMoment && this.startDateMoment.format('MM-DD')
      },
      endDateMomentWeek () {
        return this.endDateMoment && this.endDateMoment.day()
      },
      endDateMomentMonth () {
        return this.endDateMoment && this.endDateMoment.format('MM-DD')
      },
    },
    watch: {
      startDateMoment: 'refreshSelectRagne',
      endDateMoment: 'refreshSelectRagne',
      monthList: 'refreshSelectRagne',
      waiting(val) {
        this.disabled = val;
      }
    },
    methods: {
      handleConfirm() {
        if (this.singleMode || this.endDateMoment) {
          this.confirm()
        }
      },
      addMonth () {
        var monthItem = new MonthItem({
          curMonth: this.curMonth,
          disableBeforeMoment: this.disableBeforeMoment,
          disableAfterMoment: this.disableAfterMoment,
          startDateMoment: this.startDateMoment,
          endDateMoment: this.endDateMoment
        })
        this.monthList.push(monthItem)
        this.curAmount += 1
        this.curMonth.add(1, 'months')
      },
      loadRepeat () {
        var self = this
        if (!self.loadFreeze && self.showAmount > self.curAmount) {
          self.loadFreeze = true
          self.addMonth()
          setTimeout(() => {
            self.loadFreeze = false
            self.loadRepeat()
          }, 20)
        }
      },
      refreshSelectRagne () {
        var startTimeStamp = this.startDateMoment && this.startDateMoment.toDate().getTime()
        var endTimeStamp = !this.singleMode && this.endDateMoment && this.endDateMoment.toDate().getTime()
        var prefDate = {}
        this.monthList.forEach((monthData) => {
          monthData.dateList.forEach((dateData) => {
            var dateTimeStamp = dateData.timeStamp
            if (dateData.isNull) {
              dateData.isStartDate = dateData.isEndDate = false
              dateData.isProgress = (prefDate.isProgress || prefDate.isStartDate) && endTimeStamp
            } else {
              dateData.isStartDate = dateTimeStamp === startTimeStamp
              dateData.isEndDate = dateTimeStamp === endTimeStamp
              dateData.isProgress = dateTimeStamp > startTimeStamp && dateTimeStamp < endTimeStamp
            }
            prefDate = dateData
          })
        })
      },
      checkDate (date) {
        if (date.isDisable || date.isNull) {
          return
        }
        if (this.startDateMoment && (this.singleMode || this.endDateMoment)) {
          this.startDateMoment = this.endDateMoment = null
        }
        var dateData = date.dateData
        var checkTargetMoment = moment([dateData.year, dateData.month, dateData.date])
        if (!this.startDateMoment || checkTargetMoment[!this.sameEnable ? 'isSameOrBefore' : 'isBefore'](this.startDateMoment)) {
          this.startDateMoment = checkTargetMoment
        } else {
          if (!this.isSame && '' + checkTargetMoment + '' === '' + this.startDateMoment + '') {
            console.log('入离时间不能相同')
            return
          }
          this.endDateMoment = checkTargetMoment
        }
        if (this.singleMode || this.endDateMoment) {
          // this.confirm()
          this.waiting = false
        } else {
          this.waiting = true
        }
      },
      confirm () {
        var startDate = formatDate(this.startDateMoment, 'MM月DD日');
        var endDate = !this.singleMode ? formatDate(this.endDateMoment, 'MM月DD日') : undefined;
        const current = this.startDateMoment.to(this.endDateMoment);
        this.animateFreeze = true;
        const format = {
          start: this.startDateMoment.format('MM.DD') + '周' + this.weeks[this.startDateMomentWeek],
          end: this.endDateMoment.format('MM.DD') + '周' + this.weeks[this.endDateMomentWeek]
        }
        this.$emit('complete', startDate, endDate, format, current)
      }
    },
    beforeMount() {
    },
    beforeDestroy() {

    },
    mounted () {
      this.isX = browser.qq && browser.iPhoneX;
      this.$nextTick(() => {
        this.loadRepeat();
        this.scroll = new BScroll(this.$refs.datePicker, {
          scrollX: false,
          scrollY: true,
        });
      })
    }
  }
</script>

<style scoped lang="less">
.ve-picker {
  .selected-date {
    padding: 12px 20px;
    height: 46px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 20px;
    .selected-date-content {
      span {
        display: block;
        text-align: center;
      }
      span:last-child {
        height: 26px;
      }
    }
    .week-select {
      font-size: 14px;
    }
  }
  .week {
    padding: 10px 20px;
    border-top: 1px solid #E3E9E6;
    border-bottom: 1px solid #E3E9E6;
    background-color: white;
    ul {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
  }
  .select-date-picker {
    height: calc(100vh - 10rem - 46px);
    overflow-y: auto;
    #month-list {
      padding-top: 24px;
      padding-bottom: 24px;
    }
    .month-info {
      padding: 0 20px;
    }
    .month-item:first-child {
      margin-top: 0;
    }
    .month-item {
      margin-top: 20px;
      ul {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        flex-wrap: wrap;
        li {
          width: calc(100% / 7);
          height: 52px;
          line-height: 52px;
          text-align: center;
          margin-top: 4px;
        }
        li.disable {
          position: relative;
          color: #C5D1CD;
          ::before {
            content: '';
            position: absolute;
            left: 0;
            right: 0;
            top: 0;
            bottom: 0;
            margin: auto;
            display: block;
            width: 1.8rem;
            height: 0.0625rem;
            background-color: #798480;
            transform: rotate(120deg);
          }
        }
        li.today {
          width: calc(100% / 7 - 2px);
          position: relative;
          ::before {
            content: '';
            position: absolute;
            display: block;
            width: 52px;
            height: 52px;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            border-radius: 50%;
            border: 1px solid #E4ECE8;
          }
        }
        li.start-date, li.end-date, li.progress {
          color: white;
          background-color: #25A3A8;
          border: none;
          border-radius: 0;
          ::before {
            display: none;
          }
        }
        li.start-date {
          border-top-left-radius: 50%;
          border-bottom-left-radius: 50%;
        }
        li.end-date {
          border-top-right-radius: 50%;
          border-bottom-right-radius: 50%;
        }
      }
    }
  }
}
</style>