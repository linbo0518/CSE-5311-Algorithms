# <div style="text-align: center">CSE5311 Design and Analysis of Algorithms</div>

<div style="text-align: center">Bo Lin</div>
<div style="text-align: center">1001778270</div>

## (1) Exercise 2.2-1 on Page 29

**Q**:

> Express the function $\frac{n^3}{1000} - 100n^2 - 100n + 3$ in terms of $\Theta$-notation.

**A**:

We consider only the leading term of a formula. It is $\Theta(n^3)$

## (2) Exercise 3.1-1 on Page 52

**Q**:

> Let $f(n)$ and $g(n)$ be asymptotically nonnegative functions. Using the basic definition of $\Theta$-notation, prove that $max(f(n), g(n)) = \Theta(f(n) + g(n))$.

**A**:

Because $f(n)$ and $g(n)$ are asymptotically nonnegative functions, so exist $n_1$ and $n_2$ make

$f(n) \geqslant 0$ when $n > n_1$

$g(n) \geqslant 0$ when $n > n_2$

following equations are true:

$f(n) \leq max(f(n), g(n))$

$g(n) \leq max(f(n), g(n))$

$f(n) + g(n) \leq 2max(f(n), g(n))$

$0 \leq \frac{1}{2} (f(n) + g(n)) \leq max(f(n), g(n)) \leq f(n) + g(n)$

so:

$max(f(n), g(n)) = O(f(n) + g(n))$

$max(f(n), g(n)) = \Omega(f(n) + g(n))$

because:

$\Theta(f(n) + g(n)) = O(f(n) + g(n)) \cap \Omega(f(n) + g(n))$

so:

$max(f(n), g(n)) = \Theta(f(n) + g(n))$

## (3) Exercise 3.1-2 on Page 52

**Q**:

> Show that for any real constants $a$ and $b$, where $b > 0$, $(n + a)^b = \Theta(n^b)$.

**A**:

$(n + a)^b = C_{0}n^{b}a^{0} + C_{1}n^{b-1}a^{1} + ··· + C_{b}n^{0}a^{b}$

$C_0n^b \leq C_{0}n^{b}a^{0} + C_{1}n^{b-1}a^{1} + ··· + C_{b}n^{0}a^{b} \leq (C_0 + C_1 + C_2 + ··· + C_b)n^b$

So:

$(n + a)^b = \Theta(n^b)$

## (4) Problem 3.4 (b) (h) on Page 62

**Q**:

> Let $f(n)$ and $g(n)$ be asymptotically positive functions. Prove or disprove each of the following conjectures.
>
> b. $f(n) + g(n) = \Theta(min(f(n), g(n)))$.
>
> h. $f(n) + o(f(n)) = \Theta(f(n))$.

**A**:

b: Assume $f(n) = n^2$ and $g(n) = n$, so

$n^2 + n \neq \Theta(min(f(n), g(n))) = \Theta(n)$

So disprove

h: make $g(n) = o(f(n))$, so

exist $c$, $0 \leq g(n) < cf(n)$, so

$0 \leq f(n) \leq f(n) + g(n) < (c + 1)f(n)$

$0 \leq c_1f(n) \leq f(n) + o(f(n)) < c_2f(n)$

exist $c_1 = 1$ and $c_2 = c + 1$ make it prove

## (5) Exercise 4.4-2 on Page 92

**Q**:

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $T(n) = T(\frac{n}{2}) + n^2$. Use the substitution method to verify your answer.

**A**:

recursion tree method

$T(n) = \sum_{i=0}^{\lg{n}}(\frac{1}{4})^in^2$

$T(n) = n^2(1 + (\frac{1}{4}) + (\frac{1}{4})^2 +  ··· )$

$T(n) = \Theta(n^2)$

substitution method

guess $T(n) \leq cn^2$

$T(n) \leq c(\frac{n}{2})^2 + n^2$

$=\frac{c}{4}n^2 + n^2$

$=(\frac{c}{4} + 1)n^2$

$\leq cn^2$ when $c \geq \frac{4}{3}$

## (6) Exercise 4.4-4 on Page 93

**Q**:

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $T(n) = 2T(n - 1) + 1$. Use the substitution method to verify your answer.

**A**:

recursion tree method

$T(n) = \sum_{i=0}^{n-1}2^i$

$T(n) = 1 + 2 + 4 + ··· + 2^{n - 1}$

$T(n) = \Theta(2^n)$

substitution method

guess $T \leq c2^n$

$T(n) \leq 2c2^{n - 1} + 1$

$= c2^n + 1$

$= \Theta(2^n)$

## (7) Exercise 4.5-4 on Page 97

**Q**:

> Can the master method be applied to the recurrence $T(n) = 4T(\frac{n}{2}) + n^2\lg(n)$? Why or why not? Give an asymptotic upper bound for this recurrence.

**A**:

$a = 4, b = 2, n^{\log_b{a}} = n^2, f(n) = n^2\lg{n}$

$n^2\lg{n} \neq O(n^{2-\epsilon}) \neq \Omega(n^{2-\epsilon})$ so can not use master method

guess $T(n) < cn^2\lg^2{n}$

$T(n) \leq 4c\frac{1}{4}n^2\lg^2({\frac{n}{2}}) + n^2\lg(n)$

$=cn^2\lg^2(\frac{n}{2}) + n^2\lg(n)$

$=cn^2\lg(\frac{n}{2})\lg(n) - cn^2\lg(\frac{n}{2})\lg(2) + n^2\lg(n)$

$=cn^2\lg^2n - cn^2\lg{n} - cn^2\lg{n} + cn^2 + n^2\lg{n}$

$=cn^2\lg^2n + (1-2c)n^2\lg{n} + cn^2$

$\leq cn^2\lg^2{n}$

## (8) Problem 4.1 on Page 107

**Q**:

> Give asymptotic upper and lower bounds for $T(n)$ in each of the following recurrences. Assume that $T(n)$ is constant for $n \leqslant 2$. Make your bounds as tight as possible, and justify your answers.
>
> a. $T(n) = 2T(\frac{n}{2}) +n^4$.
>
> b. $T(n) = T(\frac{7n}{10}) + n$.
>
> c. $T(n) = 16T(\frac{n}{4}) + n^2$.
>
> d. $T(n) = 7T(\frac{n}{3}) + n^2$.
>
> e. $T(n) = 7T(\frac{n}{2}) + n^2$.
>
> f. $T(n) = 2T(\frac{n}{4}) + \sqrt{n}$.
>
> g. $T(n) = T(n - 2) + n^2$.

**A**:

a. use master theorem

$a=2, b=2, n^{\log_2{2}} < n^4$, so $T(n) = \Theta(n^4)$

b. use master theorem

$a=1, b=\frac{10}{7}, n^{\log_{\frac{10}{7}}{1}} < n$, so $T(n) = \Theta(n)$

c. use master theorem

$a=16, b=4, n^{\log_4{16}} = n^2$, so $T(n) = \Theta(n^2\lg{n})$

d. use master theorem

$a=7, b=3, n^{\log_3{7}} < n^2$, so $T(n) = \Theta(n^2)$

e. use master theorem

$a=7, b=2, n^{\log_2{7}} > n^2$, so $T(n) = \Theta(n^{\lg{7}})$

f. use master theorem

$a=2, b=4, n^{\log_4{2}} = \sqrt{n}$, so $T(n) = \Theta(\sqrt{n}\lg{n})$

g. 
