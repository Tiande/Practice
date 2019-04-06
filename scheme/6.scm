(define factorial
  (lambda (n)
    (if (= n 0) 1
        (* n (factorial (- n 1))))))

(factorial 4)

(define is-even?
  (lambda (n)
    (if (= n 0) #t
        (is-odd? (- n 1)))))

(define is-odd?
  (lambda (n)
    (if (= n 0) #f
        (is-even? (- n 1)))))

(letrec ((local-even? (lambda (n)
                        (if (= n 0) #t
                            (local-odd? (- n 1)))))
         (local-odd? (lambda (n)
                      (if (= n 0) #f
                          (local-even? (- n 1))))))
  (list (local-even? 23) (local-odd? 23)))

(let countdown ((i 10))
 (if (= i 0) 'liftoff
      (begin
        (display i)
        (newline)
        (countdown (- i 1)))))

(define list-position
  (lambda (o l)
    (let loop ((i 0) (l l))
      (if (null? l) #f
          (if (eqv? (car l) o) i
              (loop (+ i 1) (cdr l)))))))

(list-position 4 '(1 2 3 4))

(define reverse!
  (lambda (s)
    (let loop ((s s) (r '()))
      (if (null? s) r
          (let ((d (cdr s)))
            (set-cdr! s r)
            ; (newline)
            ; (display r)
            ; (newline)
            ; (display s)
            ; (newline)
            ; (display d)
            ; (newline)
            (loop d s))))))

(reverse! '(1 2 3 4))

(for-each display
  (list "one " "two " "buckle my shoe"))

(map cons '(1 2 3) '(10 20 30))
(map * '(1 2 3) '(4 5 6))
