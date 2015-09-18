#!/usr/bin/python

class Friends(object):
	def __init__(self,adj_dict):
		self.adj_dict=adj_dict
		
	#To make a new friend, return nothing, as non-directed, add in both
	def makeFriends(self,friend1,friend2):
		if friend1 == None or friend2 == None or len(friend1)*len(friend1)==0:
			return 'Error Input'
			
		if friend1 in self.adj_dict:
			self.adj_dict[friend1].append(friend2)
		else:
			self.adj_dict[friend1]=[friend2]
		
		if friend2 in self.adj_dict:
			self.adj_dict[friend2].append(friend1)
		else:
			self.adj_dict[friend2]=[friend1]
	
	
	#To remove a friendship on both friends side
	def removeFriends(self,friend1,friend2):
		if friend1 == None or friend2 == None or len(friend1)*len(friend1)==0:
			return 'Error Input'
		
		if friend1 in self.adj_dict and friend2 in self.adj_dict[friend1]:
			self.adj_dict[friend1].remove(friend2)
		
		if friend2 in self.adj_dict and friend1 in self.adj_dict[friend2]:
			self.adj_dict[friend2].remove(friend1)
			
	#one step BFS get all adjacent friend
	def getDirectFriends(self,friend):
		if friend ==None or len(friend)==0 or friend not in self.adj_dict:
			return None
		return self.adj_dict[friend]
	
	#set out from this guy, fetch all connected components back to me. Use DFS fetch all connected minus direct friendFriends
	def getIndirectFriends(self,friend):
		if friend ==None or len(friend)==0 or friend not in self.adj_dict:
			return None 
		self.visited=[friend]
		self.__rec_fetch(friend)		
		map(lambda x:self.visited.remove(x),self.getDirectFriends(friend))
		self.visited.remove(friend)
		return self.visited
		
	#NS DFS	
	def __rec_fetch(self,person):
		for nextPerson in self.adj_dict[person]:
			if nextPerson not in self.visited:
				self.visited.append(nextPerson)
				self.__rec_fetch(nextPerson) 
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
import unittest

class Friends_Test(unittest.TestCase):
	def setUp(self):
		self.adj_dict = {'A':['B','C','D'],'B':['A','C'],'C':['A','B','E'],'D':['A','E'],'E':['C','D']}
		self.friends=Friends(self.adj_dict)
	
	#For the initialization/constructor 	
	def test_init(self):
		self.assertTrue(len(self.friends.adj_dict)==5,"internal graphic dic should has five entry when all loaded")
		
		
	#When adding an relationship	
	def test_makeFriends1(self):
		self.friends.makeFriends('A','E')
		self.assertTrue('E' in self.friends.adj_dict['A'] and 'A' in self.friends.adj_dict['E'],"Adding A with E as friend should add a new link in both A and E entry")
	
	def test_makeFriends2(self):	
		self.friends.makeFriends('K','A')
		self.assertTrue('A' in self.friends.adj_dict['K'] and 'K' in self.friends.adj_dict['A'],"Adding A with K as friend should add a new link in both A and K entry")
		
	def test_makeFriends3(self):
		self.friends.makeFriends('T12_0000ww','W12')
		self.assertTrue('T12_0000ww' in self.friends.adj_dict['W12'] and 'W12' in self.friends.adj_dict['T12_0000ww'],"Adding two complete new strager")

	def test_makeFriends5(self):	
		self.assertTrue(self.friends.makeFriends('',None)=='Error Input',"test edge cases")
		
		
	#When removing a relationship
	def test_removeFriends1(self):
		self.assertTrue(self.friends.removeFriends('',None)=='Error Input',"test edge cases")
		
	def test_removeFriends2(self):
		self.friends.removeFriends('A','C')
		self.assertFalse('C' in self.friends.adj_dict['A'] or 'A' in self.friends.adj_dict['C'],"both are friend of each other, the edge should be removed")
	
	def test_removeFriends3(self):
		self.friends.removeFriends('A','E')
		self.assertEqual(self.friends.adj_dict, self.adj_dict,"remove two people that was not in relationship, nothing should happen")

	def test_removeFriends3(self):
		self.friends.removeFriends('K','E')
		self.assertEqual(self.friends.adj_dict, self.adj_dict,"remove two people that was not in relationship and not even exist, nothing should happen")


	#When getting direct relationship
	def test_getDirectFriends1(self):
		self.assertTrue(self.friends.getDirectFriends('')== None,"test edge cases")
		self.assertTrue(self.friends.getDirectFriends(None)== None,"test edge cases")
	
	def test_getDirectFriends2(self):
		self.assertTrue(self.friends.getDirectFriends('K')== None,"if person does not original exist, should return nothing")
	
	def test_getDirectFriends3(self):
		self.assertTrue(self.friends.getDirectFriends('C')== ['A','B','E'],"if person is an eligible person, should return a list")
		
		
	#When getting indirect relasionship
	def test_getIndirectFriends1(self):
		self.assertTrue('D' in self.friends.getIndirectFriends('C'),"getting indrect friends of C, shoud have D. D is only indirect person with C")
	
	def test_getIndirectFriends2(self):
		self.assertEqual(self.friends.getIndirectFriends(None),None,"Edge cases")
		self.assertEqual(self.friends.getIndirectFriends(""),None,"Edge cases")
		self.assertEqual(self.friends.getIndirectFriends('W123sa12dsa0000s  adsf'),None,"Edge cases")

if __name__ == '__main__':
	unittest.main()
