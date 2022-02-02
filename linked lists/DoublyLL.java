package week4;

public class DoublyLL<T> {
    private DoublyLLNode<T> front;
    private DoublyLLNode<T> tail;
    public DoublyLL(){
        front = null;
        tail = null;
    }
    public void insert(DoublyLLNode<T> newNode, DoublyLLNode<T> prevNode){
        if (prevNode == null){
            newNode.setNext(front);;
            front = newNode;
            front.setPrev(null);
        } else {
            DoublyLLNode<T> nextNode = prevNode.getNext();
            newNode.setNext(nextNode);
            prevNode.setNext(newNode);
            newNode.setPrev(prevNode);
        }
    }
    public boolean delete(DoublyLLNode<T> targetNode){
        DoublyLLNode<T> currNode = front;
        DoublyLLNode<T> prevNode = null;
        DoublyLLNode<T> nextNode = null;
        while ((currNode != prevNode) && (currNode != targetNode)){
            prevNode = currNode;
            currNode = currNode.getNext();
        }
        if (currNode == null) {
            return false;
        } else {
            if (prevNode != null){
                nextNode = currNode.getNext();
                prevNode.setNext(nextNode);
                nextNode.setPrev(prevNode);
            }
            else
                front = front.getNext();
                return true;
        }
    }

}

