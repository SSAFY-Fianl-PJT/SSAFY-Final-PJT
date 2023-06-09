import api from '@/api/base.js'
import { fetchLogin, fetchLogout, fetchSignup, tk2Ur, fetchUsrInfo } from '@/api/user'

export default {
    state : {
        token: null,
        info : null,
        profile : null,
        profile4wishList: null
    },
    getters: {
        isLogin(state) {
            if (state.token === null){
                api.clearToken()
            }else{
                api.setToken(state.token)
            }
            return state.token ? true : false
        },

    },
    mutations:{
        SAVE_TOKEN(state, token) {
            state.token = token
        },
        SAVE_USERINFO(state, info) {
            state.info = info
        },
        SAVE_USER_Profile(state, prof){
            state.profile = prof
        },
        SAVE_USER_Profile4wishList(state,prof){
            state.profile4wishList = prof
        }
    },
    actions:{
        async signUp(context, payload) {
            const username = payload.username
            const nickname = payload.nickname
            const password1 = payload.password1
            const password2 = payload.password2
            await fetchSignup({username, nickname, password1, password2})
            .then((res) => {
                context.commit('SAVE_TOKEN', res.data.key )
            })
            .catch((err) => {
                console.log(err)
            })
        },
        async get_usr_name(context){
            await tk2Ur().then((res) => { 
                context.commit('SAVE_USERINFO', res.data )
            })
        },
        async get_profile(context, username) {
            
            await fetchUsrInfo({username}).then((res) => { 
              console.log("찾았나",res);
              context.commit('SAVE_USER_Profile', res.data);
            })
          },
        async get_profile4wishList(context, username){
            await fetchUsrInfo({username}).then((res) => { 
                console.log(res);
                context.commit('SAVE_USER_Profile4wishList', res.data);
              })
        },
        async login(context, payload) {
            const username = payload.username
            const password = payload.password

            await fetchLogin({ username, password })
            .then((res) => {
                context.commit('SAVE_TOKEN', res.data.key)
                console.log(res.data)
            })
            .catch((err) => {
                console.log(err)})
        },

        async logout(context){
            await fetchLogout()
            .then(() => {
                context.commit('SAVE_TOKEN', null)
                localStorage.removeItem('user.token')
            })
            .catch((err) => console.log(err))
        }
    }
}