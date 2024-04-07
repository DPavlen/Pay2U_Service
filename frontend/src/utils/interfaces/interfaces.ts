// Прошу считать все странные наименования и не логичные сплетения интерфейсов проблемой бэкендеров

export interface IService {
  id: number;
  name: string;
  link: string;
  category: ICategoryShort;
  icon_big: string;
  icon_square: string;
  icon_small: string;
  is_popuar: boolean;
}

export interface IServiceExtended extends IService {
  category: ICategory;
  description: string;
  tariff: ITariff[];
}

export interface IServiceCategory {
  category?: ICategory;
  services: IServiceExtended[];
}

export interface ISubscription {
  id: number;
  user: number;
  tariff: ITariffExtended;
  is_active: boolean;
  expired_date: string;
  auto_payment: boolean;
  created_at: string;
  updated_at: string;
}

export interface ITariff {
  id: number;
  name: string;
  tariff_full_price: number;
  tariff_promo_price: number;
  services_duration: string;
  description: string;
}

export interface ITariffExtended extends ITariff {
  services: IService;
}

export interface ICashback {
  id: number;
  serviceId: number;
  type_cashback: 'percentage' | 'fixed_amount';
  amountCashback: number;
}

export interface ICashbackSubscription {
  tariffId: number;
  userId: number;
  paymentId: number;
  accruedСashback: number;
  status: 'cashback_completed' | 'cashback_not_received';
}

export interface ICategory {
  id: number;
  name: string;
  slug: string;
  description: string;
  icon: string;
}

export interface ICategoryShort {
  name: string;
  slug: string;
}

export interface IUser {
  //TODO где-от приходит full_name, где-то по оттельности
  id: number;
  email: string;
  username: string;
  first_name?: string;
  last_name?: string;
  full_name?: string;
  first_enter?: boolean;
}

export interface IPaymentMethod {
  id: number;
  payment_method: string;
  methodName?: string;
  priorityMethod?: boolean;
  icon: string;
  user: IUser;
}

export interface IPurchseShippingFields {
  tariffId: number;
  paymentMethodId: number;
  subscriptionId: number;
  autopayment: boolean;
  terms: boolean;
  politics: boolean;
}

export interface ISearchShippingFields {
  query: string;
}

export interface IPayment {
  id: number;
  subscription: ISubscription;
  payment_methods: IPaymentMethod;
  cost: string;
  date: string;
  expired_date: string;
  status: 'payment_completed' | 'not_paid';
  cashback?: ICashbackSubscription;
}

export interface IFaq {
  id: number;
  topic_question: string;
  question: string;
  answer: string;
  created: string;
  updated: string;
}
