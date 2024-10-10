# Avalonia入门指南

## 数据双向绑定

### 传统方法

> 传统方法基于`avalonia`自己的实现。不需要使用第三方的接口

#### 优点: 

1. 不用下载`ReactiveUI`
2. 不依赖`Reactive Object`

#### 缺点:

1. 使用较为复杂

#### 使用方法

1. 继承 `INotifyPropertyChanged `接口
2. 重写`PropertyChanged` 事件
3. 使用set属性通知更改

#### 完整代码

```c#
public partial class MainWindowViewModel : INotifyPropertyChanged {
    public event PropertyChangedEventHandler? PropertyChanged;
    
    private double _px, _py;
    public double Px {
        get => _px;
        set {
            _px = value;
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nameof(Px)));
        }
    }
}
```

### ReactiveUI

> 该方法需要将`ReactiveUI`添加到解决方案的依赖里

#### 优点

1. 使用简单

#### 缺点

1. 依赖`Reactive Object`

#### 使用方法

1. 添加`ReactiveUI`的依赖  `dotnet add package Avalonia.ReactiveUI `
2. 将`ViewModel`继承`ReactiveObject`类
3. 使用`RaiseAndSetIfChanged` 更新数据

#### 完整代码

```c#
public partial class MainWindowViewModel : ReactiveObject {
    private double _px, _py;

    public double Px {
        get => _px;
        set => this.RaiseAndSetIfChanged(ref _px, value);
    }
    
    public double Py {
        get => _py;
        set => this.RaiseAndSetIfChanged(ref _py, value);
    }
}
```



## 路由

> 使用`ReactiveUI`进行路由管理

### 使用

1. 添加依赖 `dotnet add package Avalonia.ReactiveUI` 

2. ViewModel 需要继承 `ReactiveObject, IRoutableViewModel` 

   完整代码

   ```c#
   public partial class SettingWindowViewModel(IScreen screen) : ReactiveObject, IRoutableViewModel {
       public IScreen HostScreen { get; } = screen;
   
       // 可路由视图模型的唯一标识符。
       public string UrlPathSegment { get; } = Guid.NewGuid().ToString().Substring(0, 5);
   }
   ```

3. view 界面需要使用`UserControl` 然后View类需要继承`ReactiveUserControl`。泛型需要添加ViewModel

   完整代码

   ```c#
   public partial class SettingWindowView : ReactiveUserControl<SettingWindowViewModel> {
       public SettingWindowView() {
           AvaloniaXamlLoader.Load(this);
       }
   }
   ```

4. `MainWindowsViewModel`需要继承`ReactiveObject, IScreen` 处理路由

   ```c#
   public partial class MainWindowViewModel : ReactiveObject, IScreen {
       public RoutingState Router { get; } = new();
       public ReactiveCommand<Unit, IRoutableViewModel> GoNext { get; }
       public ReactiveCommand<Unit, IRoutableViewModel?> GoBack => Router.NavigateBack;
   
       /**
        * 设置下一步
        */
       public MainWindowViewModel() {
           GoNext = ReactiveCommand.CreateFromObservable(() => Router.Navigate.Execute(new SettingWindowViewModel(this)));
       }
   }
   ```

5. smartsem

yidontek
