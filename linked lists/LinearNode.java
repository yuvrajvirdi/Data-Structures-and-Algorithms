package week4;

public class LinearNode <T>{
     // because a node will point to another node, of type T
    private LinearNode<T> next; 
    private T dataItem;
    public LinearNode(){
        next = null;
        dataItem = null;

    }
    public LinearNode(T value){
        next = null;
        dataItem = value;
    }
    public LinearNode<T> getNext(){
        return next;
    }
    public void setNext(LinearNode<T> node){
        next = node;
    }
    public T getDataItem(){
        return dataItem;
    }
    public void setDataItem (T value) {
        dataItem = value;
    }
    public static void main(String[] args) {
        Integer obj =  new Integer(7);
        LinearNode<Integer> iNode =  new LinearNode<Integer>(obj);
    }
}
