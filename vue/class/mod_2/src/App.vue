<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-30 09:22:10
 * @LastEditTime: 2023-12-03 21:43:46
 * @Description: 初始化
-->
<template>
  <div id="top_bar">
    <van-icon name="arrow-left" size="20px" />
    <span style="font-size: 20px">计算机学院学生去向调查</span>
  </div>
  <van-form @submit="onSubmit">
    <!-- 学号手机号 -->
    <van-cell-group inset>
      <van-field v-model="sno" label="学号" placeholder="请输入学号" :rules="sno_rule" />
      <van-field v-model="pho" label="手机号" placeholder="请输入手机号" :rules="phone_rule" />

      <!-- 专业 -->
      <van-field
        v-model="major"
        is-link
        readonly
        label="专业"
        placeholder="请选择专业"
        @click="show_major_picker = true"
        :rules="required_rule"
      />

      <van-popup v-model:show="show_major_picker" position="bottom">
        <van-picker
          :columns="major_columns"
          @confirm="onMajorConfirm"
          @cancel="show_major_picker = false"
        />
      </van-popup>

      <!-- 年级 -->
      <van-field
        v-model="grade"
        is-link
        readonly
        label="年级"
        placeholder="请选择年级"
        @click="show_grade_picker = true"
        :rules="required_rule"
      />

      <van-popup v-model:show="show_grade_picker" position="bottom">
        <van-picker
          :columns="grade_columns"
          @confirm="onGradeConfirm"
          @cancel="show_grade_picker = false"
        />
      </van-popup>

      <!-- 离开日期 -->
      <van-field
        v-model="leave_date"
        is-link
        readonly
        label="离开时间"
        placeholder="选择离开时间"
        @click="show_leave_date_picker = true"
        :rules="required_rule"
      />
      <van-calendar
        :min-date="new Date('2023-9-28')"
        :max-date="new Date('2023-10-8')"
        v-model:show="show_leave_date_picker"
        @confirm="onLeaveDateConfirm"
      />

      <!-- 返程日期 -->
      <van-field
        v-model="back_date"
        is-link
        readonly
        label="返程时间"
        placeholder="选择返程时间"
        @click="show_back_date_picker = true"
        :rules="required_rule"
      />
      <van-calendar
        :min-date="new Date('2023-9-28')"
        :max-date="new Date('2023-10-8')"
        v-model:show="show_back_date_picker"
        @confirm="onBackDateConfirm"
      />
    </van-cell-group>
    <div style="margin: 16px">
      <van-button round block type="primary" native-type="submit"> 提交 </van-button>
    </div>
  </van-form>

  <!-- 显示结果 -->
  <van-popup v-model:show="show_result" position="center" style="width: 100%; max-width: 400px">
    <van-cell-group inset>
      <van-cell title="学号" :value="sno" />
      <van-cell title="手机号" :value="pho" />
      <van-cell title="专业" :value="major" />
      <van-cell title="年级" :value="grade" />
      <van-cell title="离开日期" :value="leave_date" />
      <van-cell title="返程日期" :value="back_date" />
    </van-cell-group>
  </van-popup>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { showDialog } from 'vant';

const sno = ref(''); // 学号
const pho = ref(''); // 手机号
const major = ref(''); // 专业
const grade = ref(''); // 年级
const leave_date = ref(''); // 离开日期
const back_date = ref(''); // 返程日期

// 学号校验
const sno_rule = [
  {
    required: true,
    message: '请输入正确的学号',
    pattern: /^[0-9a-zA-Z]\d{8}$/
  }
];

// 必填校验
const required_rule = [
  {
    required: true,
    message: '该选项不可为空!'
  }
];

// 手机号校验
const phone_rule = [
  {
    required: true,
    message: '请输入正确的电话号码',
    pattern: /^1[3456789]\d{9}$/
  }
];

/* 展示组件 */
const show_major_picker = ref(false);
const show_grade_picker = ref(false);
const show_leave_date_picker = ref(false);
const show_back_date_picker = ref(false);
const show_result = ref(false);

// 年级信息
const grade_columns = [
  { text: '大一', value: 'one grade' },
  { text: '大二', value: 'two grade' },
  { text: '大三', value: 'three grade' },
  { text: '大四', value: 'four grade' }
];

// 专业信息
const major_columns = [
  { text: '算机科学与技术', value: 'Computer Science' },
  { text: '软件工程', value: 'Software Engineering' },
  { text: '网络工程', value: 'Network Engineering' },
  { text: '数字媒体技术', value: 'Digital Media Technology' },
  { text: '物联网工程', value: 'Internet of Things Engineering' },
  { text: '数据科学与大数据技术', value: 'Data Science and Big Data Technology' }
];

// 专业确认
const onMajorConfirm = ({ selectedOptions }: any) => {
  major.value = selectedOptions[0]?.text;
  show_major_picker.value = false;
};

// 年级确认
const onGradeConfirm = ({ selectedOptions }: any) => {
  grade.value = selectedOptions[0]?.text;
  show_grade_picker.value = false;
};

// 格式化日期
const formatDate = (date: any) => {
  let year = date.getFullYear();
  let month = `${date.getMonth() + 1}`.padStart(2, '0');
  let day = `${date.getDate()}`.padStart(2, '0');
  return `${year}-${month}-${day}`;
};

// 离开确认
const onLeaveDateConfirm = (date: any) => {
  leave_date.value = formatDate(date);
  show_leave_date_picker.value = false;
};

// 返程确认
const onBackDateConfirm = (date: any) => {
  back_date.value = formatDate(date);
  show_back_date_picker.value = false;
};

// 提交
const onSubmit = () => {
  let leave = new Date(leave_date.value);
  let back = new Date(back_date.value);
  if (back < leave) {
    showDialog({
      message: '返程日期小于离开日期!',
      theme: 'round-button'
    });
  } else {
    show_result.value = true;
  }
};
</script>
