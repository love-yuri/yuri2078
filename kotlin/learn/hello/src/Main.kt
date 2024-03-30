
class Person {
    var name = ""
    fun sayHello() {
        println("Hello, $name!")
    }
}

fun main() {
    // val 不可变, var 可变, const 常量
    val name = "Kotlin"

    val getVal = { value: String -> Int
        println("yuri $value")
        1
    }

    println("name -> $name, val ${getVal("is yes")}")

    val person: Person = Person().apply {
        this.name = "yuri is yes"
        sayHello()
    }

    println("personName -> ${person.name}")

    val strLen = { str: String -> Int
        str.length
    }
    println("yuri size -> ${strLen("yuri is yes")}")
}