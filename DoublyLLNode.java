package week4;

public class DoublyLLNode<T> {
    private DoublyLLNode<T> next;
    private DoublyLLNode<T> prev;
    private T dataItem;
    public DoublyLLNode(){
        next = null;
        prev = null;
        dataItem = null;
    }
    public DoublyLLNode(T value){
        next = null;
        prev = null;
        dataItem = value;
    }
    public DoublyLLNode<T> getNext(){
        return next;
    }
    public void setNext(DoublyLLNode<T> node){
        next = node;
    }
    public DoublyLLNode<T> getPrev(){
        return prev;
    }
    public void setPrev( DoublyLLNode<T> node){
        prev = node;
    }
    public T getDataItem(){
        return dataItem;
    }
    public void setDataItem(T value){
        dataItem = value;
    }
}
