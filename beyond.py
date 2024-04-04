from dataclasses import dataclass

from typing import List, Tuple, Dict, ClassVar

from timeit import timeit

@dataclass(slots=True)
class Term:
	sid: int
	type: int # 1 is a constat or a functor, 2 is a variable
	args: Tuple
	table: ClassVar

	def __str__(self):
		return f'{Term.table[self.sid]+ ("."+str(self.sid) if self.is_variable() else "")}{"" if not self.args else "("+",".join(map(str,self.args))+")"}' 

	def is_variable(self):
		return self.type == 2


@dataclass(slots=True)
class TQF:
	quantifier: int # 1 is forall, 2 is exists
	variables: List
	conjunct: List
	next: List

	def is_forall():
		return self.quantifier == 1

	def is_exists():
		return self.quantifier == 2


@daaclass(slots=True)
class Question:
	tqf
	context


@dataclass(slots=True)
class Context:
	m: Dict


@dataclass(slots=True)
class ReverseNode:
	e_atom
	top_aformula







Term.table = {1:"a", 2:"x",3:"f",4:"h"}

t1 = Term(1,1,())
t1x = Term(1,1,())
t2 = Term(2,2,())

t3 = Term(3,1,(t1,t1x,t2))
t4 = Term(3,1,(t1x,t1x,t2))

t5 = Term(4,1,(t3,t2))
t6 = Term(4,1,(t4,t2))


print(t5)
print(t6)
print(t5 == t6)
print(Term.table)