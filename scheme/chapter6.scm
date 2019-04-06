; ; ; (let ((i 1) (j 2))
; ; ;   (+ i j))

; ; ; (let ((i 1))
; ; ;   (let ((j (+ i 2)))
; ; ;     (* i j)))

; ; ; (let* ((i 1) (j (+ i 2)))
; ; ;   (* i j))

; ; ; (define (list*2 ls)
; ; ;   (if (null? ls)
; ; ;       '()
; ; ;       (cons (* 2 (car ls))
; ; ;             (list*2 (cdr ls)))))

; ; ; (list*2 (list 1 2 3))

; ; (define (my-length ls)
; ;   (if (null? ls)
; ;         0
; ;         (+ 1 (my-length (cdr ls)))))

; ; (my-length (list 1 2 3))

; ; (define (my-sum ls)
; ;   (if (null? ls)
; ;       0
; ;       (+ (car ls) (my-sum (cdr ls)))))

; ; (my-sum (list 1 2 3 ))

; ; (define (remove x ls)
; ;   (if (null? ls)
; ;       '()
; ;       (let ((h (car ls)))
; ;         ((if (eqv? x h)
; ;             (lambda (y) y)
; ;             (lambda (y) (cons h y)))
; ;          (remove x (cdr ls))))))

; ; (define (remove-x ls x)
; ;   (if (null? ls)
; ;       '()
; ;       (if (not (eqv? x (car ls)))
; ;           (cons (car ls) (remove-x (cdr ls) x))
; ;           (remove-x (cdr ls) x))))

; ; (remove-x (list 1 2 3) 2)
; ; (remove-x (list 1 2 3 1 2 3 1 2 3 1 2 3) 2)

; (define (index-x ls x)
;   (if (null? ls)
;       '()
;       (if (null? (cdr ls))
;           #f 
;           (if (not (eqv? x (car ls)))
;               (+ 1 (index-x (cdr ls) x))
;               0))))

; (index-x (list 1 2 3) 2)
; (index-x (list 1 2 3) 4)

; (define (position x ls)
;   (position-aux x ls 0))

; (define (position-aux x ls i)
;   (cond
;    ((null? ls) #f)
;    ((eqv? x (car ls)) i)
;    (else (position-aux x (cdr ls) (1+ i)))))

; (define (lengthls ls)
;   (length ls))
; (lengthls (list 1 2 3 4))

(define (my-reverse ls)  
  (my-reverse-help ls '())))

(define (my-reverse-help ls0 ls1)
  (if (null? ls0)
      ls1
      (my-reverse-help (cdr ls0) (cons (car ls0) ls1)))))

(my-reverse (list 1 2 3 4))


(define )
