const { createApp, ref, onBeforeMount } = Vue;
const { showDialog } = vant;

const ticket_count = ref(1); // 购票数量 
const show = ref(false); // 显示时间控件
const show_time = ref(false); // 显示时间label
const date = ref(''); // 日期
const show_dialog = ref(false); // 显示购票信息


const imgs = ref(attrations); // 图片信息
const index = ref(0); // 当前图片下标
// 上一张
const pre_img = () => {
    index.value--;
    if (index.value < 0) {
        index.value = imgs.value.length - 1;
    }
}

// 下一张
const next_img = () => {
    index.value++;
    if (index.value == imgs.value.length) {
        index.value = 0;
    }
}

// 选择日期后
const onConfirm = (value) => {
    let year = value.getFullYear();
    let month = value.getMonth() + 1;
    let day = value.getDate();
    date.value = `${year}-${month}-${day}`;
    show.value = false;
    show_time.value = true;
}

// 获取后30天日期
const max_date = () => {
    const currentDate = new Date();
    const currentTime = currentDate.getTime(); // 获取当前时间
    // 计算30天后的时间戳
    const thirtyDaysLaterTime = currentTime + 30 * 24 * 60 * 60 * 1000; // 30天的毫秒数
    return new Date(thirtyDaysLaterTime);
}

// 点击购买后
const buy = () => {
    if (date.value != null && date.value != "") {
        show_dialog.value = true;
    } else {
        showDialog({
            message: '请选择时间',
            theme: 'round-button',
        });
    }
}

// 点击购买处理
const confirm = () => {
    showDialog({
        message: '购买成功',
        theme: 'round-button',
    });
}

// 取消购买处理
const cancel = () => {
    showDialog({
        message: '取消成功',
        theme: 'round-button',
    });
}

const App = {
    data() {
        return {
            imgs, next_img, pre_img, index,
            ticket_count, date, show, onConfirm,
            show_time, show_dialog, confirm, cancel,
            buy, max_date
        };
    },
};
const app = Vue.createApp(App);
app.use(vant);
app.mount("#app");