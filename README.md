# Mersenne numbers, Lucas Lehmer test, and Sieve of Eratosthenes
Author: Tochukwu Emmanuel Okafor

LinkedIn: https://linkedin.com/in/tochukwuokafor/

Twitter: @toch_okafor

E-mail: okafor.tochukwu93@gmail.com

Date: 13 October 2019

In this repository, I develop functions for mersenne numbers, the Lucas Lehmer test, and the Sieve of Eratosthenes. Along the way, optimized methods of generating prime numbers are developed and implemented.

# Mersenne numbers

A mersenne number is a number that is one less than a power of two.

M = 2^n - 1 where n is an integer and M is a Mersenne number.

The search for Mersenne primes is one of the most computationally intensive and actively pursued areas of advanced and distributed computing (Wolfram MathWorld, 2019).

# Lucas Lehmer test

In mathematics, the Lucas Lehmer test is a primality test for Mersenne numbers. It is an efficient deterministic primality test for determining if a Mersenne number is prime. You can read more about it here: http://mathworld.wolfram.com/Lucas-LehmerTest.html and here: https://www.maths.tcd.ie/pub/ims/bull54/M5402.pdf

# Applications of Lucas Lehmer test

The test is used by the Great Internet Mersenne Prime Search (GIMPS) to locate large primes. This search has been successful in locating many of the largest primes known to date. The test is considered valuable because it can probably test a large set of very large numbers for primality within an affordable amount of time. In contrast, the equivalently fast Pépin's test for any Fermat number can only be used on a much smaller set of very large numbers before reaching computational limits.

# Sieve of Eratosthenes

The Sieve of Eratosthenes is an old and simple algorithm for listing all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime. This is the sieve's key distinction from using trial division to sequentially test each candidate number for divisibility by each prime

# Applications of Sieve of Eratosthenes

The Sieve of Eratosthenes is an application of dynamic programming and it forms a fundamental part of the number theory. You can read more about it here: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Copyright: Kindly contact me if you wish to reproduce any of my codes in part or in full. Thanks!
