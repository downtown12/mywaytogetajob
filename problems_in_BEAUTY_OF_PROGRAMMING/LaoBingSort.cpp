#include<cassert>
#include<iostream>
using namespace std;

class LaoBingSorting{
	private:
		int *m_CakeArray;	//烙饼信息数组，存储烙饼序列初始状态的数组
		int m_nCakeCnt;		//烙饼个数
		int m_nMaxSwap;		//最多翻转次数，即上届

		int *m_SwapArray;	//交换结果数组，即保存最优解的每一步交换

		int *m_ReverseCakeArray;//当前翻转信息数组
		int *m_ReverseCakeArraySwap;//当前交换结果数组
		int m_nSearch;		//当前遍历次数信息
		//上述“当前”均指在搜索最优解的过程中的某一时刻
	
	public:
		LaoBingSorting()
		{
			m_nCakeCnt = 0;
			m_nMaxSwap = 0;
			//m_nSearch = 0;
		}
		~LaoBingSorting()
		{
			if(m_CakeArray != NULL)
				delete m_CakeArray;
			if(m_SwapArray != NULL)
				delete m_SwapArray;
			if(m_ReverseCakeArray != NULL)
				delete m_ReverseCakeArray;
			if(m_ReverseCakeArraySwap != NULL)
				delete m_ReverseCakeArraySwap;
		}

		/*开始寻找最优解*/
		void Run(int * pCakeArray, int nCakeCnt)
		{

			Init(pCakeArray, nCakeCnt);
			m_nSearch = 0;
			Search(0);
		}

		void Output()
		{
			cout<<"依次翻转烙饼序列中序号如下的烙饼："<<endl;

			for(int i = 0; i< m_nMaxSwap; i++)
				cout<<m_SwapArray[i]<<" ";

			cout<<"\nSearch Times: "<<m_nSearch<<endl;
			cout<<"Total Swap Times: "<<m_nMaxSwap<<endl;
		}

	private:
		void Init(int *pCakeArray, int nCakeCnt)
		{
			assert(pCakeArray != NULL);
			assert(nCakeCnt > 0);

			m_nCakeCnt = nCakeCnt;

			m_CakeArray = new int[nCakeCnt];
			assert(pCakeArray != NULL);
			for(int i = 0; i<nCakeCnt; i++){
				m_CakeArray[i] = pCakeArray[i];
			}

			m_nMaxSwap = UpperBound(m_nCakeCnt);

			m_SwapArray = new int[m_nMaxSwap];
			assert(m_SwapArray != NULL);

			m_ReverseCakeArray = new int[m_nCakeCnt];
			assert(m_ReverseCakeArray != NULL);
			for(int i = 0; i<m_nCakeCnt; i++){
				m_ReverseCakeArray[i] = pCakeArray[i];
			}
			m_ReverseCakeArraySwap = new int[m_nMaxSwap];
		}

		/*计算上界*/
		int UpperBound(int nCakeCnt)
		{
			return (nCakeCnt -1) * 2;
		}

		/*计算下界*/
		int LowerBound(int* pCakeArray, int nCakeCnt)
		{
			int t;
			int ret = 0;
			for(int i = 1; i<nCakeCnt; i++){
				t = pCakeArray[i] - pCakeArray[i-1];
				if(t == 1 || t == -1)
				{
				}
				else{
					ret++;
				}
			}
			return ret;
		}

		void Search(int step)
		{
			int i, nEstimate;
		
			m_nSearch++;

			//剪枝，估算本次输入的最少翻转次数
			nEstimate = step + LowerBound(m_CakeArray, m_nCakeCnt);
			if(nEstimate > m_nMaxSwap)
				return;
			
			//若已排序，输出结果
			if(IsSorted(m_ReverseCakeArray, m_nCakeCnt)){
				if(step < m_nMaxSwap){
					m_nMaxSwap = step;
					for(i = 0; i<m_nMaxSwap; i++)
						m_SwapArray[i] = m_ReverseCakeArraySwap[i];
				}
				return;
			}

			//递归搜索结果
			for(int i = 1;i<m_nCakeCnt;i++){
				Reverse(0,i);
				m_ReverseCakeArraySwap[step] = i;
				Search(step+1);
				Reverse(0,i);
			}

		}

		/*判断是否已经排好序*/
		bool IsSorted(int * pCakeArray, int nCakeCnt)
		{
			for(int i = 1; i<nCakeCnt; i++ ){
				if(pCakeArray[i-1] > pCakeArray[i])
					return false;
			}
			return true;
		}
		
		/*翻转烙饼*/
		void Reverse(int nBegin, int nEnd)
		{
			assert(nBegin < nEnd);
			int i, j, t;

			for(i = nBegin, j = nEnd; i<j; i++, j--){
				t = m_ReverseCakeArray[i];
				m_ReverseCakeArray[i] = m_ReverseCakeArray[j];
				m_ReverseCakeArray[j] = t;
			}
		}
};

int main()
{
	//int a [] = {3, 1, 2, 4};
	int a [] = {3, 2, 1, 6, 5, 4, 9, 8, 7, 0};
	const int a_length = 10;
	class LaoBingSorting lb;
	lb.Run(a, a_length);
	lb.Output();

	return 0;
}
