# API Rest Binary Tree

We extend the concept of linked data structures to a structure containing nodes
with more than one self-referenced field. A binary tree is made of nodes, where each node contains a "left" reference, a
"right" reference, and a data element. The topmost node in the tree is called the root.
Every node (excluding a root) in a tree is connected by a directed edge from exactly one other node. This node is called
a parent. On the other hand, each node can be connected to an arbitrary number of nodes, called children. Nodes with no
children are called leaves, or external nodes. Nodes that are not leaves are called internal nodes. Nodes with the same
parent are called siblings.

“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant of itself).”

## Installation

You can clone the project in your local machine

```bash
git clone https://github.com/SebastianCalle/API-Rest-BinaryTree.git
 ```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install requirements.txt
```

## Usage
Run the server in your local machine and open the in your browser. [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
```python
python manage.py runserver
```
The URLs that are available:
- [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) Show the URLs that are available.
- [http://127.0.0.1:8000/api/create](http://127.0.0.1:8000/api/create) Create Binary Tree using a string where the first number is the Root, and the others are the nodes of the tree that are separate by commas. Ex: "23,34,5,6,7,8"
- [http://127.0.0.1:8000/api/list](http://127.0.0.1:8000/api/list) List all Binary Trees that are stored in Data Bases.
- [http://127.0.0.1:8000/api/lca](http://127.0.0.1:8000/api/lca) This returns the value of the Lowest Common Ancestor between 2 nodes. For this is necessary that the first parameter is ID of the Tree and the second and third are the nodes to search the ancestor separated by commas. Ex: "7f7f2b4c-4b7f-45e1-b098-37a041feda04,2,3"

## Features
One interesting feature is when you create or search the lowest common ancestor in a Tree, This is graphical in the console how you can see.

![Image of Yaktocat](https://i.ibb.co/HHx6Lzy/graphical-Binary.png)
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)