from dataclasses import dataclass

from typing import List, Tuple, ClassVar


@dataclass(slots=True, frozen=True)
class Term:
	sid: int
	type: int # 1 is a constat or a functor, 2 is a variable
	args: Tuple
	table: ClassVar

	def __str__(self):
		return f'{Term.table[self.sid]+ ("."+str(self.sid) if self.type==2 else "")}{"" if not self.args else "("+",".join(map(str,self.args))+")"}' 


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