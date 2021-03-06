public class BinaryHeap <Key extends Comparable<Key>>{
    private Key[] pq;
    private int N;
    public BinaryHeap(int capacity){
        pq=(Key[]) new Comparable[capacity+1];
    }
    public boolean isEmpty(){
        return N == 0 ;
    }
    public void insert(Key key){}
    public Key deleteMax(){
        Key max = pq[1];
        exchange(1,N--);
        sink(1);
        pq[N+1] = null;
        return max;
    }

    private void sink(int k){
        while (2*k <= N){
            int j = 2*k;
            if (j<N && less(j,j+1))
                j++;
            if (!less(k,j))
                break;
            exchange(k,j);
            k=j;
        }
    }

    private boolean less( int i, int j ){
        return pq[i].compareTo(pq[j]) < 0;
    }
    private void exchange(int i, int j){
        Key t =  pq[i];
        pq[i] = pq[j];
        pq[j] = t;
    }

}

    
