(progn
  (define fact (lambda (x)
    (if (> x 0)
	(* x (fact (- x 1)))
      (1))))
  (define foo (lambda (bar) bar))
  (if (foo 't)
      (+ 2 1)
    (foo 42)))

