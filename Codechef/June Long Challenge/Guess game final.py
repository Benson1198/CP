def guessg(start1,end1,start2,end2):
    if(start1<=end1 and start2<=end2):
        mid=(start1+end2)//2
        print(mid)
        c=input()
        if(c=='E'):
            return -1
        if(c=='G'):
            count=0
            prev='L'
            while(start1<=end1 and start2<=end2):
                mid1=(start1+end1)//2
                mid2=(start2+end2)//2
                print(mid1)
                c1=input()
                if(c1=='E'):
                    return -1
                elif(c1=='G' and count==0):
                    return guessg(mid1+1,end1,start2,end2)
                count=1
                if(c1=='L' and prev=='G'):
                    end1=mid1-1
                if(c1==prev and c1=='G'):
                    start1=mid1+1
                    return guessg(start1,end1,start2,end2)

                print(mid2)
                c2=input()
                prev=c2
                if(c2=='E'):
                    return -1
                elif(c1==c2):
                    if(c1=='L'):
                        end2=mid2-1 
                    else:
                        start1=mid1+1
                    return guessg(start1,end1,start2,end2)
                elif(c1=='L' and c2=='G'):
                    end1=mid1-1
                    start2=mid2+1
                

        else:
            count=0
            prev='G'
            while(start1<=end1 and start2<=end2):
                mid1=(start1+end1)//2
                mid2=(start2+end2)//2
                print(mid2)
                c1=input()
                if(c1=='E'):
                    return -1
                elif(c1=='L' and count==0):
                    return guessg(start1,end1,start2,mid2-1)
                count=1
                if(c1=='G' and prev=='L'):
                    start2=mid2+1
                    
                if(c1==prev and c1=='L'):
                    end2=mid2-1
                    return guessg(start1,end1,start2,end2)


                print(mid1)
                c2=input()
                prev=c2
                if(c2=='E'):
                    return -1
                elif(c1==c2):
                    if(c1=='G'):
                        start1=mid1+1
                    else:
                        end2=mid2-1
                    return guessg(start1,end1,start2,end2)
                elif(c1=='G' and c2=='L'):
                    end1=mid1-1
                    start2=mid2+1

    if(start1>end1 and start2<=end2):
        guessg(start2,(start2+end2)//2,(start2+end2)//2,end2)
    elif(start2>end2 and start1<=end1):
        guessg(start1,(start1+end1)//2,(start1+end1)//2,end1)


n = int(input())
guessg(1,n//2,n//2,n)