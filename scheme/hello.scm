; (define a 10)
; (define b 20)
; ; (when (< a b)
; (unless (> a b)
;   (newline)
;   (display "a is ")
;   (display a)
;   (newline)
;   (display "b is ")
;   (display b)
;   (newline)
;   (display "a is bigger than b"))

; (define c #\c)
; (cond ((char<? c #\c) -1)
;       ((char=? c #\c) 0)
;       (else 1))

; (define c #\c)
; (case c
;   ((#\a) 1)
;   ((#\b) 2)
;   ((#\c) 3)
;   (else 4))

(define x 9)
(set! x 20)
(let ((x 1)
      (y 2)
      (z 3))
  (list x y z))

(let ((x 1)
       (y x))
  (+ x y))

(let* ((x 1)
       (y x))
  (+ x y))

(let ((cons (lambda (x y) (* x y))))
  (cons 3 2))

(cons 3 2)

(define counter 0)

(define bump-counter
  (lambda ()
    (set! counter (+ counter 1))
    counter))

(bump-counter)
(bump-counter)
(bump-counter)

(fluid-let ((counter 99))
           (display (bump-counter)) (newline)
           (display (bump-counter)) (newline)
           (display (bump-counter)) (newline))

counter
