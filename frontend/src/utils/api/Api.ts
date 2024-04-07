import axios from 'axios';
import { IPurchseShippingFields } from '../interfaces/interfaces';

class Api {
  private apiToken: string;
  baseUrl: string;

  constructor(baseUrl: string) {
    this.apiToken = localStorage.getItem('apiToken') || '';
    this.baseUrl = baseUrl;
  }
  private requester() {
    return axios.create({
      baseURL: this.baseUrl,
      headers: {
        Authorization: `Token ${this.apiToken}`,
      },
    });
  }

  login = (username: string, password: string) =>
    this.requester()
      .post(
        '/auth/token/login/',
        { username, password },
        { headers: { Authorization: '' } }
      )
      .then(({ data }) => data);

  getUserData = () =>
    this.requester()
      .get('/v1/users/me', {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  getPaymentMethods = () =>
    this.requester()
      .get('/v1/payment_methods', {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  getUserSubscriptions = () =>
    this.requester()
      .get('/v1/subscriptions', {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  getAllServicesList = () =>
    this.requester()
      .get('/v1/services', {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  getCategorizedServicesList = (name: string) =>
    this.requester()
      .get(`/v1/services/?category=${name}`, {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      // TODO вернуть обратно после исправления бека
      // .get(`/v1/categories/${id}/services`)
      .then(({ data }) => data);

  getPopularServices = () =>
    this.requester()
      .get(`/v1/services/popular`, {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  getService = (id: number) =>
    this.requester()
      .get(`/v1/services/${id}`, {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  getCategoriesList = () =>
    this.requester()
      .get(`/v1/categories`, {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  getFaq = () =>
    this.requester()
      .get(`/v1/faqs`, {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  searchServicesByQuery = (query: string) =>
    this.requester()
      .get(`/v1/services?name=${query}`, {
        headers: {
          Authorization: `Token ${localStorage.getItem('apiToken')}`,
        },
      })
      .then(({ data }) => data);

  purchase = (data: IPurchseShippingFields) =>
    this.requester()
      .post(
        `/v1/services/${data.subscriptionId}/add/`,
        {
          tariff_id: data.tariffId,
          payment_methods: data.paymentMethodId,
          auto_payment: data.autopayment,
        },
        {
          headers: {
            Authorization: `Token ${localStorage.getItem('apiToken')}`,
          },
        }
      )
      .then(({ data }) => data);
}

const api = new Api('http://localhost:8000/api/');

export default api;
