# Copyright 2025 D.G. MacCarthy <https://github.com/dmaccarthy>
#
# This file is part of "sal_cs".
#
# "sal_cs" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "sal_cs" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "sal_cs".  If not, see <https://www.gnu.org/licenses/>.


"""
CSE 2110: Procedural Programming
Pre- & Post-Conditions

"""

def smallestFactor(n: int) -> int:
	"Calculate the smallest factor of a natural number"
	f = 2
	while f * f <= n:
		if n % f == 0: return f
		f += 1
	return n

def isPrime(n: int) -> bool:
	"Check whether a number is prime"
	return n > 1 and smallestFactor(n) == n

def primes(howMany: int = 20) -> list:
	"Make a list of prime numbers"
	p = 2
	primes = []
	while howMany:
		if isPrime(p):
			primes.append(p)
			howMany -= 1
		p += 1
	return primes

def factor(n: int) -> list:
	"Make a list of a number's prime factors"
	factors = [1] if n == 1 else []
	while n > 1:
		f = smallestFactor(n)
		factors.append(f)
		n //= f
	return factors
