# Android开发基础

> 基于kotlin

## ImageView

1. `setImageResource` 设置资源文件id
1. `tag` 标签

## ListView

1. `layout`布局文件添加

   ```xml
   <ListView
       android:id="@+id/listView"
       app:layout_constraintTop_toBottomOf="@+id/toolbar"
       android:layout_width="match_parent"
       android:layout_height="wrap_content"
       tools:ignore="MissingConstraints" />
   ```

2. 重写 `BaseAdapter`类。

3. 重点重写`getView`函数

   ```kotlin
   override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
       // 获取 view 最后一步的false是关键，没有会报错
       val view = convertView ?: LayoutInflater.from(context).inflate(R.layout.list_view_layout, parent, false)
       val item = getItem(position)
   
       // 重新设置对象信息
       view.findViewById<TextView>(R.id.textViewTop)?.apply {
           text = item.name
       }
   
       view.findViewById<TextView>(R.id.textViewBottom)?.apply {
           text = item.number
       }
       return view
   }
   ```

4. 配置适配器

   ```kotlin
   findViewById<ListView>(R.id.listView)?.apply {
       adapter = ListViewAdapter(this@MainActivity, userList)
   }
   ```

5. 创建长按菜单

   1. 注册菜单

      ```kotlin
      findViewById<ListView>(R.id.listView)?.apply {
          this@MainActivity.registerForContextMenu(this)
      }
      ```

   2. 重写创建函数

      ```kotlin
      override fun onCreateContextMenu(
          menu: ContextMenu?,
          v: View?,
          menuInfo: ContextMenu.ContextMenuInfo?
      ) {
          super.onCreateContextMenu(menu, v, menuInfo)
          menuInflater.inflate(R.menu.main, menu)
      }
      ```

   3. 重写选择函数

      ```kotlin
      override fun onContextItemSelected(item: MenuItem): Boolean {
          val position = (item.menuInfo as AdapterView.AdapterContextMenuInfo).position
          when (item.itemId) {
              R.id.delete -> {
                  // ...
              }
              R.id.update -> {
                  // ...
              }
          }
          return super.onContextItemSelected(item)
      }
      ```

## ProgressBar

```xml
<ProgressBar
    android:layout_marginTop="20dp"
    style="?android:attr/progressBarStyleHorizontal"
    android:progress="40"
    android:max="100"
    android:layout_weight="3.0"
    android:layout_width="match_parent"
    android:layout_height="18dp"/>
```



## SQLitle

> 使用room database连接数据库

### 添加依赖

文件: build.gradle.kts

1. `plugins`下添加 `kotlin("kapt")`

2. `dependencies`下添加

   ```ceylon
   val room_version = "2.6.1"
   
   implementation("androidx.room:room-runtime:$room_version")
   annotationProcessor("androidx.room:room-compiler:$room_version")
   
   // To use Kotlin annotation processing tool (kapt)
   kapt("androidx.room:room-compiler:$room_version")
   // To use Kotlin Symbol Processing (KSP)
   ksp("androidx.room:room-compiler:$room_version")
   
   // optional - Kotlin Extensions and Coroutines support for Room
   implementation("androidx.room:room-ktx:$room_version")
   
   // optional - RxJava2 support for Room
   implementation("androidx.room:room-rxjava2:$room_version")
   
   // optional - RxJava3 support for Room
   implementation("androidx.room:room-rxjava3:$room_version")
   
   // optional - Guava support for Room, including Optional and ListenableFuture
   implementation("androidx.room:room-guava:$room_version")
   
   // optional - Test helpers
   testImplementation("androidx.room:room-testing:$room_version")
   
   // optional - Paging 3 Integration
   implementation("androidx.room:room-paging:$room_version")
   ```

### 编写实体类

```kotlin
@Entity
data class User(
    @PrimaryKey val name: String,
    @ColumnInfo(name = "avatar") @DrawableRes val avatar: Int,
    @ColumnInfo(name = "number") val number: String,
    @ColumnInfo(name = "address") val address: String,
)
```

### 编写DAO接口

```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM user")
    fun getAll(): List<User>

    @Query("SELECT * FROM user where name = :name limit 1")
    fun findByName(name: String): User?

    @Insert
    fun insert(user: User)

    @Update
    fun update(user: User)

    @Delete
    fun delete(user: User)
}
```

### 编写数据库

```kotlin
@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

### 开始处理

```kotlin
// 创建数据库
db = Room.databaseBuilder(
    context,
    AppDatabase::class.java, "users.db"
).allowMainThreadQueries().fallbackToDestructiveMigration().build()

// 获取dao
val userDao = db.userDao()

// 然后就可以使用dao的方法来操作数据库了
```

## AppCompatActivity

1. `setContentView(R.layout.activity_main)` 设置显示的主界面
2. `setSupportActionBar(findViewById(R.id.toolbar))` 设置toolbar
3. `this@MainActivity.startActivity(Intent(this@MainActivity, SaveUserActivity::class.java))` 界面跳转

## Intent

1. `putExtra("name", name)` 添加扩展参数
2. `intent.getBooleanExtra("isUpdate", false)` 获取扩展参数

## 布局常用属性



# Kotlin开发基础

## 常用函数

1. `Random.nextInt(int: Int)` 随机生成一个值, 如果传入参数则是 0 - n

## 多线程基础

1. 获取协程`private val mainScope = CoroutineScope(Dispatchers.Main)`

2. 执行任务

   ```kotlin
   mainScope.launch {
       while (count < progressBar.max) {
           delay(1000)
           count++
           withContext(Dispatchers.Main) {
               textView?.apply {
                   text = "$count%"
                   translationX = (count / 100.0f * width) - 80
               }
               progressBar?.setProgress(count)
           }
       }
   }
   ```

3. `withContext` 切换回主线程执行任务
