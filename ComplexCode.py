public class ComplexClient 
{
	public static void main (String[] args)
	{
	Complex c1 = new Complex(1,2);
	Complex c2 = new Complex(7,-5);
	Complex c3 = c1.add(c2);
	Complex c4 = c1.multBy(c2);
	System.out.println(c3);
	}
}




public class Complex 
{

	private int real;
	private int imag;
	
	public Complex(int real, int imag)
	{
		this.real = real;
		this.imag = imag;
	}
	
	public int getReal()
	{
		return real;
	}
	
	public int getImag()
	{
		return imag;
	}

	public void setReal(int r)
	{
		real = r;
	}
	
	public Complex add(Complex other)
	{
		int sumReal = this.real + other.real;
		int sumImag = this.imag + other.imag;
		Complex sum = new Complex(sumReal, sumImag);
		return sum;
	}
	
	public Complex multBy(Complex other2)
	{
		int sumReal = this.real * other2.real;
		int sumImag = this.imag * other2.imag;
		Complex end = new Complex(sumReal,sumImag);
		return end;
	}
	
	public String toString()
	{
		return this.real + "+" + this.imag + "i";
	}
}

