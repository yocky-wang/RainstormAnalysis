export const toPingyin = (name)=>{
  switch(name){
    case '广东':
      return 'guangdong'
    case '浙江':
      return 'zhejiang'
    case '安徽':
      return 'anhui'
    case '江苏':
      return 'jiangsu'
    case '河北':
      return 'hebei'
    case '北京':
      return 'beijing'
    case '天津':
      return 'tianjin'
    case '上海':
      return 'shanghai'
    default:
      return 'china'
  }
}