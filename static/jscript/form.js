console.log("entered")
let button=document.querySelectorAll('.btn');
let turn='O';
let c=0;
const h1=document.querySelector('h1');
h1.innerText='djsdfkjsd'
const btn=document.querySelector('.reset');
btn.innerText='reload'
const winnerset=[
    [0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]
];

function stop (){
button.forEach((b)=>{
    b.disabled=true;});
}
button.forEach((b) => {
    b.addEventListener('click',()=>{
        // c+=1;
        if(turn==='O'){
            b.innerText='O';
            turn='X';
        } 
        else{
            b.innerText='X';
            turn='O';
        }
        c=findwin(c);
        alert('c');
        b.disabled=true;
        
    });   
});
btn.addEventListener('click',()=>{
  resetf(); 
});

function findwin(c){
     winnerset.forEach((ele)=>{
        let res;
        if(button[ele[0]].innerText!=''&& button[ele[1]].innerText!='' && button[ele[2]].innerText!=''){
                if(button[ele[0]].innerText===button[ele[1]].innerText &&button[ele[0]].innerText ===button[ele[2]].innerText){
                // console.log("winner is ",ele[0]);
                res=ele[0];
                stop();
                let e=document.createElement("p");
                h1.append(e);
                e.setAttribute("class","win")
                // e.style.classList.remove('win');

                let temp=document.querySelector('.win');
                temp.style.color="pink";
                temp.innerText="winner is "+button[ele[0]].innerText;
                
              
            }
            else{
                
                if (c/2=== 0){
                    
                    console.log("c==9 block ",c);
                    prompt(c);
                    let e=document.createElement("p");
                h1.append(e);
                e.setAttribute("class","win")
                // e.style.classList.remove('win');

                try{let temp=document.querySelector('.win');
                temp.style.color="pink";
                temp.innerText="MATCH DRAW ";}
                catch(err){
                    prompt(err);
                }
                return 0;
            }
            
        }
    }});
    return c;
}
                


function resetf(){
    
    turn="O";
    button.forEach((b)=>{
        b.disabled=false;
        b.innerText="";
        
       
        
        
    });
    let temp=document.querySelector('.win');
    temp.remove();
    
    

}
 