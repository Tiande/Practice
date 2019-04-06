(call-with-input-file "hello.txt"
                      (lambda (i)
                        (let* ((a (read-char i))
                               (b (read-char i))
                               (c (read-char i)))
                          (list a b c))))

