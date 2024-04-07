from dataclasses import dataclass

from typing import List, Tuple, Dict, ClassVar, Any

from timeit import timeit


@dataclass(slots=True, unsafe_hash=True)
class Term:
	sid: int
	type: int # 1 is a constat or a functor, 2 is a variable
	args: Tuple
	table: ClassVar
	print_mode: ClassVar = "plain"

	def __str__(self):
		if Term.print_mode == "verbose":
			return f'{Term.table[self.sid]+ ("."+str(self.sid) if self.is_variable() else "")}{"" if not self.args else "("+",".join(map(str,self.args))+")"}' 
		if Term.print_mode == "plain":
			return f'{Term.table[self.sid]}{"" if not self.args else "("+",".join(map(str,self.args))+")"}' 

	def is_variable(self):
		return self.type == 2


@dataclass(slots=True)
class Flatterm:
	vector: List[Tuple[int,int]]


@dataclass(slots=True)
class VMap:
	m: Dict

	def get_map(self, v):
		return self.m[v] if v in self.m else None

	def check_v(self, v):
		return v in self.m

	def add(self, v, t):
		self.m[v] = t

	def __str__(self):
		return "{" + ", ".join(map(lambda p: str(p[0]) + " -> " + str(p[1]), self.m.items())) + "}"




@dataclass(slots=True)
class TQF:
	quantifier: int # 1 is forall, 2 is exists
	variables: List
	conjunct: List
	prev: Any
	next: List
	inverted: List

	def is_forall():
		return self.quantifier == 1

	def is_exists():
		return self.quantifier == 2




@dataclass(slots=True)
class Question:
	tqf: TQF
	context: VMap





def match(t_a: Term, t_e: Term, a_context: VMap, curr_answer: VMap, curr_map: VMap):
	if t_a.is_variable():
		if a_context.check_v(t_a): return match(a_context.get_map(t_a), t_e, a_context, curr_answer, curr_map)
		if curr_answer.check_v(t_a): return match(curr_answer.get_map(t_a), t_e, a_context, curr_answer, curr_map)
		if curr_map.check_v(t_a): return match(curr_map.get_map(t_a), t_e, a_context, curr_answer, curr_map)
		curr_map.add(t_a,t_e)
		return True
	if t_a.sid == t_e.sid:
		for p in list(zip(t_a.args, t_e.args)):
			if not match(p[0], p[1], a_context, curr_answer, curr_map): return False
		return True
	else:
		return False


def inverted_match(t_a: Term, t_e: Term, curr_map: VMap):
	if t_a.is_variable():
		curr_map.add(t_a,t_e)
		return True
	if t_e.is_variable():
		curr_map.add(t_e,t_a)
		return True
	if t_a.sid == t_e.sid:
		for p in list(zip(t_a.args, t_e.args)):
			if not inverted_match(p[0], p[1], curr_map): return False
		return True
	else:
		return False
					






Term.table = {1:"a", 2:"x",3:"f",4:"h",5:"e", 6:"y"}

t1 = Term(1,1,())
t1x = Term(1,1,())
t2 = Term(2,2,())
t_e = Term(5,1,())

t3 = Term(3,1,(t1,t1x,t2))
t4 = Term(3,1,(t1x,t1x,t_e))

t_y = Term(6,2,())

t5 = Term(4,1,(t3,t_y))
t6 = Term(4,1,(t4,t1))


print(t5)
print(t6)
print(t5 == t6)
print(Term.table)

r = VMap({})
match(t5, t6, VMap({}), VMap({}), r)
print(r)




#







#