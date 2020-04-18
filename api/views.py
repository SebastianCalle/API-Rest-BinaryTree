from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BinaryTreeSerializer
from .binary import Code, insert
from binarytree import Node
from .models import BinaryTree


@api_view(['POST'])
def apiCreateTree(request):
    # View for create a Binary Tree
    data = request.data.split(',')
    root = Node(int(data[0]))
    for i in range(1, len(data)):
        insert(root, Node(int(data[i])))
    print(root)
    code = Code()
    ser = code.serialize(root)
    binary_dict = {'data': ser}
    model = BinaryTreeSerializer(data=binary_dict)
    if model.is_valid():
        tree = model.save()
    tree_dict = {
        'id': tree.id,
        'data': tree.data,
        'created': tree.created_at,
    }
    return Response(tree_dict)

@api_view(['GET'])
def apiList(request):
   tree_list = BinaryTree.objects.all()
   all_trees = []
   for tree in tree_list:
       tree_dict = {
           'id': tree.id,
           'data': tree.data,
           'created': tree.created_at,
       }
       all_trees.append(tree_dict)

   return Response(all_trees)


#@api_view(['POST'])
#def apiLowAncestor(request):

