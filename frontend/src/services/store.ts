import { configureStore } from '@reduxjs/toolkit';

import { reducer as servicesReducer } from './servicesSlice';
import { reducer as servicesCategoriesReducer } from './servicesCategoriesSlice';
import { reducer as currentUserReducer } from './currentUserSlice';
import { reducer as pageStatesReducer } from './pageStatesSlice';

export const store = configureStore({
  reducer: {
    servicesReducer,
    servicesCategoriesReducer,
    currentUserReducer,
    pageStatesReducer,
  },
  middleware: (getDefaultMiddleware) => {
    return getDefaultMiddleware();
  },
  enhancers: (getDefaultEnhancers) => {
    return getDefaultEnhancers();
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
