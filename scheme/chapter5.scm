; (define a 
;   (lambda (num)
;     (if (< num 0)
;         (- 0 num)
;         (+ 0 num))))

; (define (my-adb n)
;   (* n 
;      (if (positive? n) 1 -1)))

; (a 1)
; (a -1)
; (a 0)
; (a -1245321)


; (define b
;   (lambda (num)
;     (if (= 0 num)
;         (= 1 0)
;         (/ 1 num))))

; (define (inv n)
;   (if (not (zero? n))
;       (/ n)
;       #f))

; (b 2/3)
; (b 0)
; (b 1.5)

; (define c
;   (lambda (num)
;     (if (>= num 33)
;         (if (<= num 126)
;             (integer->char num)
;             (= 1 0))
;         (= 1 0))))

; (define (i2a n)
;   (if (<= 33 n 126)
;       (integer->char n)
;       #f))

; (c 33)
; (c 56)
; (c 12700)

(define (d num1 num2 num3)
  (and (> num1 0) (> num2 0) (> num3 0) (* num1 num2 num3)))

(d 1 2 3)

(define (pro3or a b c)
  (if (or (negative? a)
           (negative? b)
           (negative? c))
      (* a b c)
      #f))

(pro3or 1 2 3)
(pro3or 1 -2 3)

(define (e score)
  (cond 
    ((>= score 80) "A")
    ((<= 60 score 79) "B")
    ((<= 40 score 59) "C")
    ((< score 40) "D")))

(e 81)
(e 61)
(e 41)
(e 21)

eq?
eqv?
equal?

pair? 如果对象为序对则返回#t；
list? 如果对象是一个表则返回#t。要小心的是空表’()是一个表但是不是一个序对。
null? 如果对象是空表’()的话就返回#t。
symbol? 如果对象是一个符号则返回#t。
char? 如果对象是一个字符则返回#t。
string? 如果对象是一个字符串则返回#t。
number? 如果对象是一个数字则返回#t。
complex? 如果对象是一个复数则返回#t。
real? 如果对象是一个实数则返回#t。
rational? 如果对象是一个有理数则返回#t。
integer? 如果对象是一个整数则返回#t。
exact? 如果对象不是一个浮点数的话则返回#t。
inexact? 如果对象是一个浮点数的话则返回#t。

odd?、
even?、
positive?、
negative?、
zero?
