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



## SeekBar

### setOnSeekBarChangeListener

> 设置滑动进度条时的方法

```kotlin
setOnSeekBarChangeListener(object : OnSeekBarChangeListener {
    override fun onProgressChanged(
        seekBar: SeekBar?,
        progress: Int,
        fromUser: Boolean
    ) {
         // TODO("数值变化时触发")
    }

    override fun onStartTrackingTouch(seekBar: SeekBar?) {
         // TODO("开始滑动时触发")
    }

    override fun onStopTrackingTouch(seekBar: SeekBar?) {
        // TODO("停止滑动时触发")
    }
})
```

## VideoView

> 用来播放视频，常用方法和mediaPlayer差不多

1. `videoView.setVideoPath(video.path)` 设置播放路径
2. `videoView.start() 开始播放`
3. `videoView.pause()` 暂停播放

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

## 网络请求

1. 申请网络权限

   ```xml
   <uses-permission android:name="android.permission.INTERNET"/>
   ```

2. 取消http限制

   ```xml
   android:usesCleartextTraffic="true"
   ```

3. 导入依赖

   ```kotlin
   implementation ("com.squareup.retrofit2:retrofit:(2.11.0)")
   implementation ("com.squareup.retrofit2:converter-gson:2.3.0")
   implementation ("com.squareup.okhttp3:logging-interceptor:3.8.1")
   ```

4. 定义接口

   ```kotlin
   interface RetrofitService {
       @GET("yuri")
       fun hello(): Call<Student>
   }
   ```

5. 创建retrofit

   ```kotlin
   val retrofit = Retrofit.Builder()
       .baseUrl("http://192.168.184.16:8000/")
       .addConverterFactory(GsonConverterFactory.create())
       .build()
   ```

6. 创建service

   ```kotlin
   val service = retrofit.create(RetrofitService::class.java)
   service.hello().enqueue(object :retrofit2.Callback<Student> {
       // 接收到信息
       override fun onResponse(call: Call<Student>, response: Response<Student>) {
           val body = response.body()
           Log.i("yuri", "body -> $body")
       }
   
       // 调用失败
       override fun onFailure(call: Call<Student>, t: Throwable) {
           TODO("调用失败: ${t.message}")
       }
   })
   ```

7. 完整xml文件

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <manifest xmlns:android="http://schemas.android.com/apk/res/android"
       xmlns:tools="http://schemas.android.com/tools">
   
       <uses-permission android:name="android.permission.INTERNET"/>
   
   
       <application
           android:allowBackup="true"
           android:dataExtractionRules="@xml/data_extraction_rules"
           android:fullBackupContent="@xml/backup_rules"
           android:icon="@mipmap/ic_launcher"
           android:label="@string/app_name"
           android:roundIcon="@mipmap/ic_launcher_round"
           android:supportsRtl="true"
           android:theme="@style/Theme.Exp11"
           android:usesCleartextTraffic="true"
           tools:targetApi="31">
           <activity
               android:name=".MainActivity"
               android:exported="true">
               <intent-filter>
                   <action android:name="android.intent.action.MAIN" />
   
                   <category android:name="android.intent.category.LAUNCHER" />
               </intent-filter>
           </activity>
           <activity android:name=".WeatherActivity" />
       </application>
   
   </manifest>
   ```

   

## AppCompatActivity

1. `setContentView(R.layout.activity_main)` 设置显示的主界面
2. `setSupportActionBar(findViewById(R.id.toolbar))` 设置toolbar
3. `this@MainActivity.startActivity(Intent(this@MainActivity, SaveUserActivity::class.java))` 界面跳转

## Intent

1. `putExtra("name", name)` 添加扩展参数
2. `intent.getBooleanExtra("isUpdate", false)` 获取扩展参数

## MediaPlayer

> 该类是用来播放媒体的

### 播放音乐

1. `mediaPlayer.reset()` 重置资源
2. `mediaPlayer.prepare()` 准备音乐直至可以播放
3. `mediaPlayer.prepareAsync()` 异步整理音乐 
4. `mediaPlayer.start()` 开始播放音乐
5.  `mediaPlayer.pause()` 暂停音乐
6. `mediaPlayer.setDataSource(path)` 设置播放的媒体
7. `mediaPlayer.release()` 释放播放zi'yuan

## 布局常用属性

### LinearLayout

## 添加菜单

1. 在res文件夹新建menu文件夹

2. 新建一个main.xml 

3. 添加 <item title="" /> 标签

4. 重写`onCreateOptionsMenu`函数

   ```kotlin
   override fun onCreateOptionsMenu(menu: Menu?): Boolean {
       menuInflater.inflate(R.menu.main, menu)
       return super.onCreateOptionsMenu(menu)
   }
   ```

5. 设置活动bar： `setSupportActionBar(findViewById(R.id.toolbar))`

6. 重写选择事件：`onOptionsItemSelected`

## Glide

> 安卓图片加载库

1. 导入 依赖

   ```kotlin
   implementation ("com.github.bumptech.glide:glide:4.11.0")
   annotationProcessor ("com.github.bumptech.glide:compiler:4.11.0")
   implementation ("com.makeramen:roundedimageview:2.3.0")
   ```

2. 复制图片

# Kotlin开发基础

## 常用函数

1. `Random.nextInt(int: Int)` 随机生成一个值, 如果传入参数则是 0 - n

## 多线程基础

### 协程

```kotlin
// 定义之后的协程直接执行
job = lifecycleScope.launch {
    val seekBar: SeekBar = this@MusicActivity.findViewById(R.id.seekBar)
    while (::mediaPlayer.isInitialized && mediaPlayer.isPlaying) {
        // 在需要更新界面时，切换到主线程
        withContext(Dispatchers.Main) {
            val position = mediaPlayer.currentPosition.toFloat()
            seekBar.progress = (position / mediaPlayer.duration.toFloat() * 100).toInt()
        }
        delay(1000)
    }
}
```

1. 协程是直接执行的，如果不想直接执行，需要使用`launch(start = CoroutineStart.LAZY) ` 指定。然后使用job.start开始执行
2. 使用`job.cancel()` 取消协程
