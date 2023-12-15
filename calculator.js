let total2 = localStorage.getItem('total2')||0
            updateScore ()
            function calculate(num){
                total2+=num
                updateScore ()
                localStorage.setItem('total2',(total2))

            }

            function updateScore (){
                bottonValue = document.querySelector('.js-cal')
                bottonValue.innerHTML = total2
                if (!bottonValue.classList.contains('is-style'))
                {
                    bottonValue.classList.add('is-style')}
                
            }