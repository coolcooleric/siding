import java.util.ArrayList;
import java.util.List;

class ABPruning {
	static class Node {

		private String id;
		private int val = 0;
		private List<Node> children = new ArrayList<Node>();

		public Node(String id) {
			this(id, 0);
		}

		public Node(String id, int val) {
			this.id = id;
			this.val = val;
		}

		public void addChild(Node child) {
			children.add(child);
		}

		public List<Node> getChildren() {
			return this.children;
		}

		public int value() {
			return val;
		}

		public String toString() {
			return "NODE" + id;
		}
	}

	static int minMax(Node cur, int dep, int color) {
		System.out.println("visited " + cur);
		int val = Integer.MIN_VALUE;
		if (dep == 0) {
			return cur.value() * color;
		}
		for (int i = 0; i < cur.getChildren().size(); i++) {
			int tmp = -minMax(cur.getChildren().get(i), dep - 1, -color);
			val = tmp > val ? tmp : val;
		}
		return val;
	}

	static int min(Node cur, int dep) {
		System.out.println("visited " + cur);
		int val = Integer.MAX_VALUE;
		if (dep == 0) {
			return cur.value();
		}
		for (int i = 0; i < cur.getChildren().size(); i++) {
			int tmp = max(cur.getChildren().get(i), dep - 1);
			if (tmp < val) {
				val = tmp;
			}
		}
		return val;
	}

	static int max(Node cur, int dep) {
		System.out.println("visited " + cur);
		int val = Integer.MIN_VALUE;
		if (cur.getChildren().size() == 0) {
			return cur.value();
		}
		for (int i = 0; i < cur.getChildren().size(); i++) {
			int tmp = min(cur.getChildren().get(i), dep - 1);
			if (tmp > val) {
				val = tmp;
			}
		}
		return val;
	}

	static int abPruning(Node current,  int a, int b, int dep, boolean isMax) {
		System.out.println("visited " + current);
		if (dep == 0) {
			return current.value();
		}
		if (isMax) {
			for (int i = 0; i < current.getChildren().size(); i++) {
				int tmp = abPruning(current.getChildren().get(i), a, b, dep - 1, !isMax);
				a = tmp > a ? tmp : a;
				if (a >= b) {
					break;
				}
			}
			return a;
		} else {
			for (int i = 0; i < current.getChildren().size(); i++) {
				int tmp = abPruning(current.getChildren().get(i), a, b, dep - 1, !isMax);
				b = tmp < b ? tmp : b;
				if (b <= a) {
					break;
				}
			}
			return b;
		}
	}

	static int bPruning(Node current, int b, int dep) {
		System.out.println("visited " + current);
		if (dep == 0) {
			return current.value();
		}
		int val = Integer.MIN_VALUE;
		for (int i = 0; i < current.getChildren().size(); i++) {
			int tmp = aPruning(current.getChildren().get(i), val, dep - 1);
			val = tmp > val ? tmp : val;
			if (val > b) {
				break;
			}
		}
		return val;
	}

	static int aPruning(Node current, int a, int dep) {
		System.out.println("visited " + current);
		if (dep == 0) {
			return current.value();
		}
		int val = Integer.MAX_VALUE;
		for (int i = 0; i < current.getChildren().size(); i++) {
			int tmp = bPruning(current.getChildren().get(i), val, dep - 1);
			val = tmp < val ? tmp : val;
			if (val < a) {
				break;
			}
		}
		return val;
	}

	static int abPruning(Node current, int dep, int a, int b, int color) {
		System.out.println("visited " + current);
		if (dep == 0) {// or game over
			return color * current.value();
		}
		for (int i = 0; i < current.getChildren().size(); i++) {
			int tmp = -abPruning(current.getChildren().get(i), dep - 1, -b, -a,
					-color);
			a = a > tmp ? a : tmp;
			if (a >= b) {
				break;
			}
		}
		return a;
	}

	public static void main(String[] args) {
		// check b pruning
		Node a = new Node("a");

		Node b = new Node("b");
		a.addChild(b);
		Node c = new Node("c");
		a.addChild(c);

		Node d = new Node("d");
		b.addChild(d);
		Node e = new Node("e");
		b.addChild(e);
		Node f = new Node("f");
		c.addChild(f);
		Node g = new Node("g");
		c.addChild(g);
		Node h = new Node("h");
		c.addChild(h);

		Node i = new Node("i", 2);
		d.addChild(i);
		Node j = new Node("j", 1);
		d.addChild(j);
		Node k = new Node("k", 3);
		e.addChild(k);
		Node l = new Node("l", -1);
		e.addChild(l);
		Node m = new Node("m", -4);
		f.addChild(m);
		Node n = new Node("n", -2);
		f.addChild(n);
		Node o = new Node("o", -2);
		g.addChild(o);
		Node p = new Node("p", 2);
		g.addChild(p);
		Node q = new Node("q", -3);
		h.addChild(q);
		Node r = new Node("r", 5);
		h.addChild(r);

//		System.out.println(max(a, 3));
//		System.out.println(minMax(a, 3, 1));
		// min-max
		// System.out.println(max(a, 3));

		// a-b pruning
		// System.out.println(bPruning(a, Integer.MAX_VALUE, 3));
		// check a pruning
		// System.out.println(min(a, -64, 3));
		 System.out.println(abPruning(a, 3, -100, 100, 1));
//     System.out.println(abPruning(a, Integer.MIN_VALUE, Integer.MAX_VALUE, 3, true));
	}
}
