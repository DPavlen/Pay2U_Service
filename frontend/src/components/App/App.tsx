import './App.scss';
import MainPage from '../../pages/MainPage/MainPage.tsx';
import { Route, Routes, useNavigate } from 'react-router-dom';
import Layout from '../Layout/Layout.tsx';
import ErrorPage from '../../pages/ErrorPage/ErrorPage.tsx';
import { ReactElement, useEffect, useState } from 'react';
import CategoryCatalogPage from '../../pages/CategoryCatalogPage/CategoryCatalogPage.tsx';
import ServicePage from '../../pages/ServicePage/ServicePage.tsx';
import PurchasePage from '../../pages/PurchasePage/PurchasePage.tsx';
import SuccessfulPurchasePage from '../../pages/SuccessfulPurchasePage/SuccessfulPurchasePage.tsx';
import { useDispatchTyped } from '../../hooks/store.ts';
import {
  addCategorizedServices,
  addPopularServices,
} from '../../services/servicesSlice.ts';
import CategoryPage from '../../pages/CategoryPage/CategoryPage.tsx';
import UserSubscriptionsPage from '../../pages/UserSubscriptionsPage/UserSubscriptionsPage.tsx';
import { addServicesCategories } from '../../services/servicesCategoriesSlice.ts';
import {
  addCurrentUser,
  addPaymentMethods,
  addUserSubscriptions,
} from '../../services/currentUserSlice.ts';
import OnboardingPage from '../../pages/OnboardingPage/OnboardingPage.tsx';
import GuidePage from '../../pages/GuidePage/GuidePage.tsx';
import api from '../../utils/api/Api.ts';
import Loader from '../../pages/Loader/Loader.tsx';
import { setIsLoadingState } from '../../services/pageStatesSlice.ts';
import { ICategory } from '../../utils/interfaces/interfaces.ts';
import UserPaymentsPage from '../../pages/UserPaymentsPage/UserPaymentsPage.tsx';
import FaqPage from '../../pages/FaqPage/FaqPage.tsx';

function App(): ReactElement {
  const dispatch = useDispatchTyped();
  const navigate = useNavigate();
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    login();
  }, []);

  useEffect(() => {
    if (loggedIn) {
      dispatch(setIsLoadingState(true));
      Promise.all([
        api.getUserSubscriptions(),
        api.getCategoriesList(),
        api.getPopularServices(),
        api.getPaymentMethods(),
      ])
        .then(
          ([subscriptions, categories, popularServices, paymentsMethods]) => {
            dispatch(addUserSubscriptions(subscriptions));
            dispatch(addServicesCategories(categories));
            dispatch(addPopularServices(popularServices));
            dispatch(addPaymentMethods(paymentsMethods));
            getAllServicesList(categories);
          }
        )
        .catch(console.error)
        .finally(() => dispatch(setIsLoadingState(false)));
    } else {
      login();
    }
  }, [loggedIn]);

  useEffect(() => {
    const isVisited = localStorage.getItem('isVisited');
    if (!isVisited) {
      navigate('/onboarding');
      localStorage.setItem('isVisited', 'true');
    }
  }, []);
  function login() {
    api
      .getUserData()
      .then((res) => {
        dispatch(addCurrentUser(res));
        setLoggedIn(true);
      })
      .catch(() => {
        api
          .login('pavlen', '1')
          .then((res) => {
            localStorage.setItem('apiToken', res.auth_token);
            setLoggedIn(true);
          })
          .catch(console.error);
      });
  }

  function getAllServicesList(categories: ICategory[]) {
    Promise.all(
      categories.map(({ name }) => api.getCategorizedServicesList(name))
    )
      .then((servicesList) =>
        dispatch(
          addCategorizedServices(
            servicesList.map((services, index) => ({
              category: categories[index],
              services,
            }))
          )
        )
      )
      .catch(console.error);
  }

  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<MainPage />} />
        <Route path="/services/all" element={<CategoryCatalogPage />} />
        <Route
          path="/user/my-subscriptions"
          element={<UserSubscriptionsPage />}
        />
        <Route path="/user/my-payments" element={<UserPaymentsPage />} />
        <Route path="/services/category/popular" element={<CategoryPage />} />
        <Route path="/services/category/:category" element={<CategoryPage />} />
        <Route path="/services/:id" element={<ServicePage />} />
        <Route path="/purchase" element={<PurchasePage />} />
        <Route path="/faq" element={<FaqPage />} />
        <Route
          path="/successful-purchase"
          element={<SuccessfulPurchasePage />}
        />
        <Route path="/onboarding" element={<OnboardingPage />} />
        <Route path="/guide" element={<GuidePage />} />
        // TODO не забыть удалить
        <Route path="/loader" element={<Loader />} />
      </Route>
      <Route path="*" element={<ErrorPage />} />
    </Routes>
  );
}

export default App;
