class TrieNode(object):
	def __init__(self):

		self.is_word=False
		self.children=[]
		self.key=""
		self.letter=""


	def print_node(self,s):
		s+=self.letter;
		if (self.is_word==True):
			print(s)
			print(self.key)

		if (len(self.children)!=0):
			for j in range(len(self.children)):
				self.children[j].print_node(s);





class Trie(object):
	def __init__(self):
		self.root=TrieNode()


	def add(self,s,key):
		
		p=self.root
		n=len(s)
		for i in range(n):
			is_there=False
			for j in range(len(p.children)):
				if (s[i]==p.children[j].letter):
					is_there=True
					k=j

			if is_there:
				p=p.children[k];
				if (i==n-1):
					p.key=key
					p.is_word=True
					return
			else:
				new_node=TrieNode()
				if (i==n-1):
					new_node.is_word=True
					new_node.key=key

				new_node.letter=s[i]
				p.children.append(new_node)
				p=new_node


	def search(self,s):
		if (s == '\n'):
			return '00000000000000'

		p=self.root
		n=len(s)
		for i in range(len(s)):


			is_there=False;
			for j in range(len(p.children)):
				if (s[i]==p.children[j].letter):
					is_there=True
					k=j

			if (is_there==False):
				return('');
				break
			else:
				if (i==n-1) and (p.children[k].is_word):
					return(p.children[k].key)
					break
				p=p.children[k]

		return('')	


	def  prin(self):
		p=self.root;
		for i in range(len(p.children)):
			p.children[i].print_node("");



#trie.add('str','123')
#trie.add('afbwer','456')
#trie.add('abcde','678')
#trie.add('strf','234')
#trie.search('a');
#trie.search('strf');

#trie.prin()





