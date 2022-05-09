public class Calculate {
	//Please enter a number for all//
	public static int square(int num) 
	{
		int squareNum = num * num;
		return squareNum;
	}
	
	public static int cube(int num)
	{
		int cubeNum = num * num * num;
		return cubeNum;
	}
	
	public static double average(double num1, double num2)
	{
		double averageNum = (num1 * num2) / 2;
		return averageNum;
	}
	
	public static double average(double num1, double num2, double num3)
	{
		double averageNum = (num1 * num2 * num3) / 3;
		return averageNum;
	}
	
	public static double toDegrees(double radians)
	{
		double degrees = (radians * 180) / 3.14159;
		return degrees;
		
	}
	
	public static double toRadians(double degrees)
	{
		double radians = (degrees * 3.14159) / 180;
		return radians;
	}
	
	public static double discriminant (double num1, double num2, double num3)
	{
		double discriminant = ((num2 * num2) - 4*num1*num3);
		return discriminant;
	}
	
	public static String toImproperFrac(int num1, int num2, int num3)
	{
		int numer = num1*num3+num2;
		int denom = num2;
		String dash = "/";
		String sentence = numer + dash + denom;
		return sentence;
	}
	
	public static String toMixedNum(int num1, int num2)
	{
		int a = num1 / num2;
		int b = num1 % num2;
		return a + "-" + b + "/" + num2;
	}
	
	public static String foil(int a, int b, int c, int d, String var) {
		int first = a * c;
		int second = a * d;
		int third = b * c;
		int fourth = b * d;
		int added = second + third; 
		String sentence = first + var + "^2 + " + added + var + " + " + fourth;
		return sentence;
		}
	
	public static boolean isDivisibleBy(int num1, int num2)
	{
		if (num1 % num2 == 0){
			return true;
		}
		else 
		{
			return false;
					
		}
	}

	
	public static double absValue(double d)
	{
		if (d < 0){
			return Math.abs(d);
		}
		else {
			return d;
	
		}
	}
	
	public static double max(double round1, double round2)
	{
		if (round1 > round2) {
			return round1;
		}
		else {
			return round2;

		}
	}
	
	public static double min(double num1, double num2)
	{
		if (num1 < num2) {
			return num1;
		}
		else {
			return num2;

		}
	}
	
	public static double round2(double num1,int hunned) {
		if (num1 % 10 <= 5) {		
		long rounding2 = (long) Math.pow(10,hunned);
				num1 = num1 * rounding2;
				long decimals = Math.round(num1);
				double decimals2 = (double) decimals / rounding2;
				return decimals2;}
		else {
			return num1;}
		}

	public static double exponent(double base, int exp)
	{
		double answer= 1;
		for(int i = 1; i<=exp; i++)
		{
			answer *= base;
		}
		return answer;	
	}
	
	public static int factorial(int num1)
	{
		int fact = num1;
		int i = num1;
		while(i> 1)
		{
			i--;
			fact = fact * i;
		}
		return fact;
	}
	
	public static boolean isPrime(int num1)
	{
		boolean prime = true;
		int factor = 2;
		while(prime == true && factor < num1)
		{
			if(isDivisibleBy(num1,factor))
			{
				prime = false;
			}
			factor = factor + 1;	
		}
		return prime;
	}
	
	public static int gcf(int num1, int num2)
	{	
		int i = (int)max(num1, num2);
		int Factor = 1;
		while(Factor ==1 && i>=1)
		{
			if(isDivisibleBy(num1, i) && isDivisibleBy(num2, i))
			{ 
			Factor = i;
			}
			i--;
		}
		
		return Factor;
	}
	
	public static double sqrt(double num1)
	{
		double factor = num1 / 2.0;
		boolean Positive = false;
		if(num1<0)
		{
			throw new ArithmeticException("negative number");
		}
		else if (num1 == 0)
		{
			factor = 0;
		}
		else if(num1 == 1)
		{
			factor = 1;
		}
		else
		{
			while(Positive == false)
			{
				factor = (0.5) * ((num1/factor)+ factor);
				if (absValue(num1-(factor*factor))<0.005)
				{
					Positive = true;
				}
			}
		}
		factor = round2(factor, 0);
		return factor;
	}
		
		public static String quadForm(int a, int b, int c)
		{
			double disNum = discriminant(a, b, c);
			String result = "not real";
			if (disNum == 0)
			{
				result = -b / (2 * a) + "";
			}
			else if (disNum > 0)
			{
				double round1 = round2((-b + sqrt(disNum)) / (2 * a));
				double round2 = round2((-b - sqrt(disNum)) / (2 * a));
				result = min(round1, round2) + " and " + max(round1, round2);
			}
			
			return result;
		}

	public static double round2 (double decimal) {
	   double finale = 0.0;
	   int number = (int)(decimal * 100);
	  	double deci = (number / 100);
	  	double deci2 = (number / 10);
	  	if (deci2 > 4) {
	  	   deci = deci + 0.01;
	 	finale = deci;
	   }
	   else {
	 	deci2 = 0;
	 	finale = deci + deci2;
	   }
	  	return (number + finale);

	}
}





public class DoMath {

	public static void main(String[] args) {
		System.out.println(Calculate.square(2));
		System.out.println(Calculate.cube(2));
		System.out.println(Calculate.average(2,3));
		System.out.println(Calculate.average(2,3));
		System.out.println(Calculate.toDegrees(2));
		System.out.println(Calculate.toRadians(3));
		System.out.println(Calculate.discriminant(2,3,4));
		System.out.println(Calculate.toImproperFrac(2,3,4));
		System.out.println(Calculate.toMixedNum(2,3));
		System.out.println(Calculate.foil(2,3,6,-7,"x"));
		System.out.println(Calculate.isDivisibleBy(6,4));
		System.out.println(Calculate.absValue(-100));
		System.out.println(Calculate.max(2,25));
		System.out.println(Calculate.min(2,22));
		System.out.println(Calculate.round2(1.237, 2));
		System.out.println(Calculate.exponent(4.0, 2));
		System.out.println(Calculate.factorial(4));
		System.out.println(Calculate.isPrime(2));
		System.out.println(Calculate.gcf(100, 4));
		System.out.println(Calculate.sqrt(25));
	}

}
