package week4;

public class SinglyLinkedList<T> {
    private LinearNode<T> front;
    public SinglyLinkedList(){
        front = null;
    }
    public void insert(LinearNode<T> newNode,
    LinearNode<T> prevNode) {
        if (prevNode == null){
            newNode.setNext(front);
            front = newNode;
        } else {
            LinearNode<T> nextNode = prevNode.getNext();
            newNode.setNext(nextNode);
            prevNode.setNext(newNode);
        }
    }
    public boolean delete(LinearNode<T> nodeToDelete){
        LinearNode<T> currNode = front;
        LinearNode<T> prevNode = null;
        while ((currNode != prevNode) && (currNode != nodeToDelete)){
            prevNode = currNode;
            currNode = currNode.getNext();
        }
        if (currNode == null){
            return false;
        } else {
            if (prevNode != null)
                prevNode.setNext(currNode.getNext());
            else 
                front = front.getNext();
                return true;
            
        }
    }
}
