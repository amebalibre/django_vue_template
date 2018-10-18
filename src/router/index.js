import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/Home'
import blog from '@/components/Blog'
import contact from '@/components/Contact'
import details from '@/components/Details'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/blog',
      name: 'blog',
      component: blog
    },
    {
      path: '/contact',
      name: 'contact',
      component: contact
    },
    {
      path: '/details/:id',
      name: 'details',
      component: details
    }
  ]
})
