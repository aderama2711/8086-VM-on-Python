def binToHexa(n):
    
    # convert binary to int
    num = int(n, 2)
      
    # convert int to hexadecimal
    hex_num = hex(num)
    return(hex_num)

class i8086():

	def __init__(self, trace=False):
		# register
		self.reg = {
			'ax' : '0000',
			'bx' : '0000',
			'cx' : '0000',
			'dx' : '0000'
		}
		self.sp = -1 # Stack Pointer
		self.trace = trace # Trace? No? Ok
		self.cf = 0 # Carry Flag
		self.zf = 0 # Zero Flag
		self.reg_list = ['ax','bx','cx','dx']
		self.stack = []
		
	def run(self, code, ip):
		self.ip = ip # Instruction Pointer
		self.code = code # OpCode
		trace = 1
		while ( self.ip < len(self.code)):
			opcode = self.code[self.ip] # fetch instruction
			self.ip += 1
			
			# Data Transfer
			match opcode: # switch case for opcode
				case 'MOV': # currently only support for register
					reg = self.code[self.ip]
					self.ip += 1
					val = self.code[self.ip]
					self.ip += 1
					if not reg in self.reg_list: # if not a register wrong operand
						print('Wrong operand 1')
						break
						
					if val in self.reg_list: # if source is register
						val = "0x"+self.reg[val] # get value from the register
					
					if '0b' in val : # register only store in hex, so if binary we need to convert bin to hex
						val = binToHexa(val.split('0b')[1])
						
					val = val.split('0x')[1] # split 0x and the value
					if len(val) > 4: # if input more than 4 byte / 16 bit
						print('Register overflow')
						break
					if len(val) <= 4: # if input less or same than 4 byte / 16 bit
						val = '0'*(4-len(val)) + val # append 0
						
					self.reg[reg] = val
					
					trace = 3
				
				# Arithmetic
				case 'ADD': # add opcode
					op1 = self.code[self.ip] # get 1st operand
					self.ip += 1
					op2 = self.code[self.ip] # get 2nd operand
					self.ip += 1
					
					if op1 in self.reg_list: # if the destination is register
						n1 = self.reg[op1]
					else: # else = value
						n1 = op1 
						
					if op2 in self.reg_list: # if the source is register
						n2 = self.reg[op2]
					else: # else = value
						n2 = op2
					
					if op1 in self.reg_list: # if the destination is register
						result = hex(int(n1, 16) + int(n2, 16))[2:] # add 
						
						if len(result) <= 4: # if result less or same than 4 byte / 16 bit
							result = '0'*(4-len(result)) + result # append 0
						
						self.reg[op1] = result[-4:]
					
					trace = 3
					
				case 'ADC': # adc opcode
					op1 = self.code[self.ip] # get 1st operand
					self.ip += 1
					op2 = self.code[self.ip] # get 2nd operand
					self.ip += 1
					
					if op1 in self.reg_list: # if the destination is register
						n1 = self.reg[op1]
					else: # else = value
						n1 = op1 
						
					if op2 in self.reg_list: # if the source is register
						n2 = self.reg[op2]
					else: # else = value
						n2 = op2
					
					if op1 in self.reg_list: # if the destination is register
						result = hex(int(n1, 16) + int(n2, 16))[2:] # add 
						
						if len(result) <= 4: # if result less or same than 4 byte / 16 bit
							result = '0'*(4-len(result)) + result # append 0
						
						self.reg[op1] = result[-4:]
						
						if len(result) > 4: # if length greater than 4 (Carry)
							self.cf = 1
					
					trace = 3
				
				case 'SUB': # sub opcode
					op1 = self.code[self.ip] # get 1st operand
					self.ip += 1
					op2 = self.code[self.ip] # get 2nd operand
					self.ip += 1
					
					if op1 in self.reg_list: # if the destination is register
						n1 = self.reg[op1]
					else: # else = value
						n1 = op1 
						
					if op2 in self.reg_list: # if the source is register
						n2 = self.reg[op2]
					else: # else = value
						n2 = op2
					
					if op1 in self.reg_list: # if the destination is register
						result = hex(int(n1, 16) - int(n2, 16))[2:] # sub 
						
						if len(result) <= 4: # if result less or same than 4 byte / 16 bit
							result = '0'*(4-len(result)) + result # append 0
						
						self.reg[op1] = result[-4:]
					
					trace = 3
					
				case 'CMP': # cmp opcode
					op1 = self.code[self.ip] # get 1st operand
					self.ip += 1
					op2 = self.code[self.ip] # get 2nd operand
					self.ip += 1
					
					if op1 in self.reg_list: # if the destination is register
						n1 = self.reg[op1]
					else: # else = value
						n1 = op1 
						
					if op2 in self.reg_list: # if the source is register
						n2 = self.reg[op2]
					else: # else = value
						n2 = op2
						
					result = hex(int(n1, 16) - int(n2, 16))[2:] # sub 
						
					if result == 0:
						self.zf = 1
					
					trace = 3
				
				case 'INC': # inc opcode
					op1 = self.code[self.ip] # get 1st operand
					self.ip += 1
					
					if op1 in self.reg_list: # if the destination is register
						n1 = self.reg[op1]
					else: # else = value
						print('wrong operand 1 (must register)')
						break
						
					result = hex(int(n1, 16) + int(1, 16))[2:] # increment 
					self.reg[op1] = result # save new result
					
					trace = 2
					
				case 'DEC': # dec opcode
					op1 = self.code[self.ip] # get 1st operand
					self.ip += 1
					
					if op1 in self.reg_list: # if the destination is register
						n1 = self.reg[op1]
					else: # else = value
						print('wrong operand 1 (must register)')
						break
						
					result = hex(int(n1, 16) - int(1, 16))[2:] # decrement 
					self.reg[op1] = result # save new result
					
					trace = 2
					
			#trace
			if self.trace:
				print('='*10)
				print(self.code[self.ip-trace:self.ip]) # print opcode and operand depends on trace value
				for reg in self.reg: # print all register
					print(reg,':',self.reg[reg])
						
					
					
					
					
					
				
					
		
