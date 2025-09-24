fun nextM(m: Int): Int {
    return if (m % 2 == 0) m / 2 else m - 1
}

fun sumSequence(arr: List<Int>, m: Int): Int {
    var total = 0
    var cur = m
    while (cur >= 1) {
        total += arr[cur]      // M번째 원소 더하기
        if (cur == 1) break    // 1이면 종료
        cur = nextM(cur)       // 다음 M 값
    }
    return total
}

fun main() {
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    val arr = listOf(0) + readLine()!!.split(" ").map { it.toInt() }
    println(sumSequence(arr, m))
}
