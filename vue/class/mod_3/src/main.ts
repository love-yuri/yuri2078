/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-30 09:22:10
 * @LastEditTime: 2023-12-13 08:42:58
 * @Description: main ts
 */
import { createApp } from 'vue';
import './main.css';
import router from './router';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import App from './App.vue';

const app = createApp(App);
import * as ElementPlusIconsVue from '@element-plus/icons-vue';

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}
import { Sidebar, SidebarItem } from 'vant';
import {
  AddressEdit,
  AddressList,
  Area,
  Badge,
  Button,
  Card,
  Cell,
  Form,
  CellGroup,
  Checkbox,
  CheckboxGroup,
  Circle,
  Col,
  Collapse,
  CollapseItem,
  ContactCard,
  ContactEdit,
  ContactList,
  Coupon,
  CouponCell,
  CouponList,
  Dialog,
  Field,
  Icon,
  ImagePreview,
  Image,
  Lazyload,
  List,
  Loading,
  NavBar,
  NoticeBar,
  Notify,
  Overlay,
  Pagination,
  PasswordInput,
  Picker,
  Popup,
  Progress,
  PullRefresh,
  Radio,
  RadioGroup,
  Rate,
  Row,
  Calendar,
  Search,
  Slider,
  Step,
  Stepper,
  Steps,
  SubmitBar,
  Swipe,
  SwipeCell,
  SwipeItem,
  Switch,
  Tab,
  Tabbar,
  PickerGroup,
  TabbarItem,
  Tabs,
  Tag,
  Toast,
  DatePicker,
  TreeSelect,
  Uploader,
  NumberKeyboard
} from 'vant';
import 'vant/lib/index.css';
app.use(router);
app.use(AddressEdit);
app.use(AddressList);
app.use(Area);
app.use(PasswordInput);
app.use(Badge);
app.use(Button);
app.use(NumberKeyboard);
app.use(DatePicker);
app.use(Card);
app.use(Cell);
app.use(CellGroup);
app.use(Image);
app.use(Sidebar);
app.use(SidebarItem);
app.use(Checkbox);
app.use(CheckboxGroup);
app.use(Circle);
app.use(Col);
app.use(Collapse);
app.use(CollapseItem);
app.use(ContactCard);
app.use(ContactEdit);
app.use(ContactList);
app.use(Coupon);
app.use(CouponCell);
app.use(CouponList);
app.use(Dialog);
app.use(Field);
app.use(Icon);
app.use(ImagePreview);
app.use(Lazyload);
app.use(List);
app.use(Loading);
app.use(NavBar);
app.use(NoticeBar);
app.use(Notify);
app.use(Overlay);
app.use(Pagination);
app.use(PasswordInput);
app.use(Calendar);
app.use(Picker);
app.use(PickerGroup);
app.use(Popup);
app.use(Progress);
app.use(PullRefresh);
app.use(Radio);
app.use(RadioGroup);
app.use(Rate);
app.use(Row);
app.use(Search);
app.use(Slider);
app.use(Step);
app.use(Stepper);
app.use(Steps);
app.use(SubmitBar);
app.use(Swipe);
app.use(SwipeCell);
app.use(SwipeItem);
app.use(Switch);
app.use(Tab);
app.use(Tabbar);
app.use(TabbarItem);
app.use(Tabs);
app.use(Tag);
app.use(Toast);
app.use(TreeSelect);
app.use(Uploader);
app.use(ElementPlus);
app.use(Form);
app.mount('#app');
