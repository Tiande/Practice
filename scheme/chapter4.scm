; (define vhello "Hello world")
; (define fhello (lambda ()
;                  "Hello world"))
; (fhello)
; fhello

; (define hello
;   (lambda (name)
;     (string-append "Hello " name "!")))


; (define sum3
;   (lambda (a b c)
;     (+ a b c)))

; (hello "Lucy")
; (sum3 10 11 12)



; (define (sum1 num)
;   (+ 1 num))

; (sum1 3)
; (sum1 17)


; (define (de1 num)
;   (- num 1))

; (de1 3)
; (de1 17)
  

;1
(define pi (* 4 (atan 1.0)))
; pi

; degree -> radian
(define radian
  (lambda (deg)
    (* deg (/ pi 180.0))))

(radian 90)
(radian 180)
(radian 360)

