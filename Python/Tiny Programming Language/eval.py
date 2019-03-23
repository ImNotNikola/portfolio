#! /usr/bin/python

import sys

class Variable(object):

	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __repr__(self):
		return "{type = " + self.type + ", value = " +str(self.value) + "}"

class Lexer(object):

	def __init__(self, file):
		self.index = 0
		self.file = open(file, "r").read().split()
		self.token = self.file[self.index]
		self.line =1

	def match(self, c):
		if c != self.token:
			print"Syntax Errors"
			print"Line: " + str(self.line)
			sys.exit(1)
		else:
			self.lexme()
			return c

	def lexme(self):
		self.index += 1
		if self.index == len(self.file):
			self.token = ""
		else:
			self.token = self.file[self.index]
			if self.token == ";":
				self.line += 1
		return self.file[self.index-1]

	def eof(self):
		return self.token == ""

class Interperter(object):

	def prog(self):
		self.decl_list()
		self.stmt_list()

	def decl_list(self):
		if self.lex.token == 'int' or self.lex.token == 'real':
			self.decl()
			self.decl_list()

	def decl(self):
		type = self.type()
		ids = self.id_list()
		for id in ids:
			self.varmap[id] = Variable(type, None)
		self.lex.match(';')

	def type(self):
		if(self.lex.token == "int"):
			return self.lex.match("int")
		elif(self.lex.token == "real"):
			return self.lex.match("real")
		else:
			self.error("Unknown Type")

	def id_list(self):
		ids = [self.lex.lexme()]
		while(self.lex.token == ','):
			self.lex.match(',')
			ids.append(self.lex.token)
			self.lex.lexme()
		return ids

	def stmt_list(self):
		self.stmt()
		if not self.lex.eof():
			self.stmt_list()

	def stmt(self):
		if self.lex.token == 'iprint':
			self.lex.match('iprint')
			print self.expr("int")
		elif self.lex.token == 'rprint':
			self.lex.match('rprint')
			print self.expr("real")
		else:
			id = self.lex.lexme()
			self.lex.match("=")
			value = self.expr(self.varmap[id].type)
			self.varmap[id].value = value
		self.lex.match(';')

	def expr(self, expr_type):
		accum = self.term(expr_type)
		while(self.lex.token == '+' or self.lex.token == '-'):
			op = self.lex.lexme()
			right = self.term(expr_type)
			accum = self.calculate(op, accum, right)
		return accum

	def term(self, expr_type):
		accum = self.factor(expr_type)
		while(self.lex.token == '*' or self.lex.token == '/'):
			op = self.lex.token
			self.lex.lexme()
			right = self.term(expr_type)
			accum = self.calculate(op , accum, right)
		return accum

	def factor(self, expr_type):
		left = self.base(expr_type)
		if(self.lex.token == '^'):
			self.lex.match('^')
			right = self.factor(expr_type)
			return self.calculate('^', left, right)
		else:
			return left

	def base(self, expr_type):
		if self.lex.token == '(':
			self.lex.match('(')
			val = self.expr(expr_type)
			self.lex.match(')')
			return val
		elif self.is_int(self.lex.token):
			if(expr_type != "int"):
				self.error("Type Missmatch")
			else:
				return int(self.lex.lexme())
		elif self.is_real(self.lex.token):
			if expr_type != "real":
				self.error("Type Missmatch")
			else:
				return float(self.lex.lexme())
		elif self.lex.token.isalpha():
			if expr_type != self.varmap[self.lex.token].type:
				self.erro("Type Missmatch")
			else:
				return self.varmap[self.lex.lexme()].value

	def __init__(self, file):
		self.lex = Lexer(file)
		self.varmap = {}

	def error(self, msg):
		print"Error :("
		sys.exit(1)

	def calculate(self, op, left, right):
		if (op == '+'):
			return left+right
		elif (op == '-'):
			return left-right
		elif (op == '*'):
			return left*right
		elif (op == '/'):
			return left/right
		elif (op == '^'):
			return left^right
		else:
			return self.error("Unknown Operator")

	def is_int(self, num):
		try:
			int(num)
			return True
		except ValueError:
			return False
	def is_real(self, num):
		try:
			float(num)
			return True
		except ValueError:
			return False


interp = Interperter(sys.argv[1])
interp.prog()
