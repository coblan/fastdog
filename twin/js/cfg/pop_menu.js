export  var pop = {
     pop_menu(menu,x,y,scope){
    return new Promise(function(resolve,reject){

        var pop_id =new Date().getTime()
        $('body').append(`<div id="pop_${pop_id}" style="position: fixed;top:0;left:0;bottom: 0;right: 0;" @click="on_close">
                <ul :style="{top:y,left:x}" class="right-menu">
                    <li v-for="action in menu">
                        <span v-text="action.label" @click="onclick(action)"></span>
                    </li>
                </ul>
            </div>`)

        new Vue({
            el:'#pop_'+pop_id ,
            data(){
                var childStore = new Vue()
                childStore.vc = this
                return {
                    show:true,
                    menu:menu,
                    childStore:childStore,
                    x:x+'px',
                    y:y+'px',
                    scope:scope || {},
                }

            },
            watch:{
                show(nv,ov){
                    if(ov && !nv){
                        $('#pop_'+pop_id).remove()
                    }
                }
            },
            computed:{
                mystyle(){
                    return {
                        top:this.y,
                        left:this.x,
                    }
                }
            },
            methods:{
                onclick(item){
                  if(item.action){
                      ex.eval(item.action,scope)
                  }
                },
                close(){
                    this.show = false
                },
                on_finish(e){
                    this.show=false
                    resolve(e)
                },
                on_close(){
                    $('#pop_'+pop_id).remove()
                }
            }
        })
    })
},
    prompt(){
        return new Promise((resolve,reject)=>{
            layer.prompt(function(val, index){
                //layer.msg('得到了'+val);
                resolve(val)
                layer.close(index);
            });
        })

    }
}