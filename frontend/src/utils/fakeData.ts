// import book from '../images/icons/books.svg';
// import music from '../images/icons/music.svg';
// import health from '../images/icons/heart.svg';
// import video from '../images/icons/video.svg';
// import userImage from '../images/other_images/user.jpg';
// import paymentMethodLogo1 from '../images/logos/sbp_logo.png';
// import paymentMethodLogo2 from '../images/logos/master-card_logo.png';
// import { ICategory, IUser } from './interfaces/interfaces.ts';
//
// export const userApiToken = '2744066fd74d6a5fc73feb732d904efbe701284b'
//
// export const currentUser: IUser = {
//   userId: 1,
//   fullName: 'Иван Иванов',
//   phone: '+75551234567',
//   email: 'WfNkN@example.com',
//   login: 'login',
//   userIcon: userImage,
//   paymentMethods: [
//     {
//       id: 1,
//       methodName: 'СБП',
//       methodToken: 'card',
//       priorityMethod: true,
//       methodIcon: paymentMethodLogo1,
//     },
//     {
//       id: 2,
//       methodName: 'MasterCard **** 1324',
//       methodToken: 'card',
//       priorityMethod: false,
//       methodIcon: paymentMethodLogo2,
//     },
//   ],
// };
//
// export const subscriptionsCategoriesData: ICategory[] = [
//   {
//     id: 0,
//     name: 'Книги',
//     slug: 'books',
//     description: 'Книги по подписке',
//     icon: book,
//   },
//   {
//     id: 1,
//     name: 'Музыка',
//     slug: 'music',
//     description: 'Музыка по подписке',
//     icon: music,
//   },
//   {
//     id: 2,
//     name: 'Здоровье',
//     slug: 'health',
//     description: 'Здоровье по подписке',
//     icon: health,
//   },
//   {
//     id: 3,
//     name: 'Кино',
//     slug: 'movies',
//     description: 'Кино по подписке',
//     icon: video,
//   },
//   {
//     id: 4,
//     name: 'Развлечения',
//     slug: 'entertainment',
//     description: 'Кино по подписке',
//     icon: video,
//   },
// ];
//
// // export const subscriptionsData: ISubscription[] = [
//   // {
//   //   id: 0,
//   //   name: 'Кинопоиск',
//   //   category: [
//   //     {
//   //       id: 1,
//   //       slug: 'books',
//   //       name: 'имя категории',
//   //       description: 'описание категории',
//   //       icon: book,
//   //     },
//   //   ],
//   //   link: 'ya.ru',
//   //   serviceIconBig: serviceBig,
//   //   serviceIconSquare: serviceSquare,
//   //   serviceIconSmall: serviceSmall,
//   //   serviceDetails:
//   //     'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
//   //   serviceTariffList: [
//   //     {
//   //       tariffId: 1,
//   //       tariffName: '1 месяц',
//   //       tariffDescription: '',
//   //       tariffPromoPrice: 199,
//   //       tariffFullPrice: 399,
//   //       tariffDuration: 1,
//   //     },
//   //     {
//   //       tariffId: 2,
//   //       tariffName: '6 месяцев',
//   //       tariffDescription: '',
//   //       tariffPromoPrice: 1998,
//   //       tariffFullPrice: 2394,
//   //       tariffDuration: 6,
//   //     },
//   //     {
//   //       tariffId: 3,
//   //       tariffName: '12 месяцев',
//   //       tariffDescription: '',
//   //       tariffPromoPrice: 3996,
//   //       tariffFullPrice: 4788,
//   //       tariffDuration: 12,
//   //     },
//   //   ],
//   // },
// //   {
// //     id: 1,
// //     name: 'Яндекс.Плюс',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: book,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 2,
// //     name: 'Иви',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: book,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 2,
// //     name: 'Окко',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: book,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 2,
// //     name: 'Яндекс.Плюс',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: music,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 2,
// //     name: 'Кинопоиск',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: music,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 3,
// //     name: 'Кинопоиск',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: music,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 3,
// //     name: 'Кинопоиск',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: music,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 3,
// //     name: 'Подписка на 6 месяцов',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: video,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 4,
// //     name: 'Подписка на 6 месяцов',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: video,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 4,
// //     name: 'Подписка на 6 месяцов',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: video,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// //   {
// //     id: 4,
// //     name: 'Подписка на 6 месяцов',
// //     category: [
// //       {
// //         id: 1,
// //         slug: 'books',
// //         name: 'имя категории',
// //         description: 'описание категории',
// //         icon: video,
// //       },
// //     ],
// //     link: 'ya.ru',
// //     serviceIconBig: serviceBig,
// //     serviceIconSquare: serviceSquare,
// //     serviceIconSmall: serviceSmall,
// //     serviceDetails:
// //       'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tristique tortor tortor. Aenean eget lectus nulla. Nullam et velit rutrum felis laoreet sagittis sed ultrices nibh. Phasellus id massa enim. Proin congue pellentesque magna, et fringilla arcu mollis at. Sed vitae nunc pulvinar est dignissim malesuada sit amet at justo.',
// //     serviceTariffList: [
// //       {
// //         tariffId: 1,
// //         tariffName: '1 месяц',
// //         tariffDescription: '',
// //         tariffPromoPrice: 199,
// //         tariffFullPrice: 399,
// //         tariffDuration: 1,
// //       },
// //       {
// //         tariffId: 2,
// //         tariffName: '6 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 1998,
// //         tariffFullPrice: 2394,
// //         tariffDuration: 6,
// //       },
// //       {
// //         tariffId: 3,
// //         tariffName: '12 месяцев',
// //         tariffDescription: '',
// //         tariffPromoPrice: 3996,
// //         tariffFullPrice: 4788,
// //         tariffDuration: 12,
// //       },
// //     ],
// //   },
// // ];
