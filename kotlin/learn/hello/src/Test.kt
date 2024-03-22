class MyClass {
    private var _string = "default value"

    val string: String
        get() = _string
}

fun main() {
    val myClass = MyClass()
    println(myClass.string) // 输出 "default value"
}
