
class Node(object):
    def __init__(self,word,explain):
        self.word = word
        self.explain = explain
        self.left = self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,word,explain):
        global size
        size += 1
        if self.root == None:
            self.root=Node(word,explain)
        else:
            self._insert(word,explain,self.root)

    def _insert(self,word,explain,cur_node):
        global size
        global llen
        if word < cur_node.word:
            if cur_node.left == None:
                cur_node.left=Node(word,explain)
            else:
                self._insert(word,explain,cur_node.left)

        elif word > cur_node.word:
            if cur_node.right == None:
                cur_node.right=Node(word,explain)
            else:
                self._insert(word,explain,cur_node.right)
        else:
            # print("Value is already in tree!")
            size -= 1
            cur_node.explain = cur_node.explain+" // " + explain

    def find(self,word):
        if self.root!=None:
            answer = self._find(word, self.root)
            return answer.word, answer.explain
        else:
            return

    def _find(self,word,cur_node):
        if word==cur_node.word:
            return cur_node
        elif word < cur_node.word and cur_node.left!=None:
            return self._find(word,cur_node.left)
        elif word > cur_node.word and cur_node.right!=None:
            return self._find(word,cur_node.right)

        print("[ Not Found ]")


    def printree(self):
        if self.root!=None:
            self._printree(self.root)

    def _printree(self,cur_node):
        global cnt
        if cur_node!=None:
            self._printree(cur_node.left)
            print(cur_node.word)
            print(cur_node.explain)
            cnt += 1
            self._printree(cur_node.right)

    def Size(self):
        global size
        print("이진검색트리에 저장된 단어의 갯수는",size,"개 입니다.")


    def getsuc(self,node):
        current = node

        while(current.left is not None):
            current = current.left

        return current


    def delete(self,word):
        global size
        if self.root == None:
            print("해당 단어는 존재하지 않습니다.")
            return False
        else:
            self._delete(self.root,word)
            size -= 1
            # print("성공적으로 삭제하였습니다!")


    def _delete(self,cur_node,word):

        if word < cur_node.word:
            cur_node.left = self._delete(cur_node.left,word)

        elif( word > cur_node.word ):
            cur_node.right = self._delete(cur_node.right,word)

        else:

            if cur_node.left is None:
                temp = cur_node.right
                cur_node = None
                return temp
            elif cur_node.right is None:
                temp = cur_node.left
                cur_node = None
                return temp


            temp = self.getsuc(cur_node.right)

            cur_node.word = temp.word

            cur_node.right = self._delete(cur_node.right,temp.word)

        return cur_node

def deletefind(filename):
    words = []
    data = open(filename, mode='r', encoding="utf-8")
    while True:
        isspace_sen_se = data.readline()
        if not isspace_sen_se: break
        sen = isspace_sen_se.split('\n')[0]
        words.append(sen)

    words = list(set(words))

    return words



if __name__=="__main__":
    cnt = 0
    size = 0
    tree = BinarySearchTree()

    while True:
        commend = input("$ ")

        if len(commend.split()) == 2:
            second = commend.split()[1]

        first = commend.split()[0]

        if first == "read":
            data = open("shuffled_dict.txt", mode='r', encoding="utf-8")

            while True:
                isspace_sen = data.readline()
                if not isspace_sen: break
                sen = isspace_sen.split('\n')[0]
                word = sen.split('(')[0]
                nword = word.split()[0]
                explain = sen.split(')')[1]
                tree.insert(nword, explain)
            ori_size = size

        if first == "add":
            add_word = input("word : ")
            input("class: ")
            add_meaning = input("meaning: ")
            tree.insert(add_word,add_meaning)

        if first == "find":
            print(tree.find(second))

        if first == "delete":
            var1,var2 = tree.find(second)
            tree.delete(var1)
            print("성공적으로 삭제하였습니다!")
            # tree.printree()

        if first == "size":
            tree.Size()

        if first == "deleteall":
            check_list = deletefind(second)
            for i in check_list:
                tree.delete(i)
            putthis = ori_size - size
            print(str(putthis)+ " words were deleted successfully.")

        if first == "print":
            tree.printree()


    # tree.Size()
    # tree.printree()
    # print(cnt)

    # nword, nexplain = tree.find("Travel")
    # print(nword, ":",nexplain)

    # var1,var2 = tree.find("worthwhile")
    # tree.delete(var1)
    # tree.printree()
    #
    # tree.insert("dog", "animal" )
    # tree.insert("cat", "animal1")
    # tree.insert("zebra", "animal2")
    # tree.insert("bird","animal3")
    # tree.insert("pig","animal4")
    # tree.insert("horse","animal5")
    # tree.insert("lion","animal6")
    # tree.insert("tiger","animal7")
    # tree.insert("hobeam","멋진팀원")
    # tree.insert("superGO","팀장-신출귀몰")
    # tree.insert("subi","수비수")
    #
    # tree.printree()
    # print("-------------------")
    # tree.size()
    # print("-------------------")
    # print(tree.find("dog"))
    # print(tree.find("butterfly"))
