import {
  IPayment,
  IPaymentMethod,
  ISubscription,
  IUser,
} from '../utils/interfaces/interfaces.ts';
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface ICurrentUserState {
  currentUser: IUser;
  userSubscriptions: ISubscription[];
  paymentMethods: IPaymentMethod[];
  paymentHistory: IPayment[];
}

const initialState: ICurrentUserState = {
  currentUser: {} as IUser,
  userSubscriptions: [],
  paymentMethods: [],
  paymentHistory: [],
};

const currentUserSlice = createSlice({
  name: 'currentUser',
  initialState,
  reducers: {
    addCurrentUser: (state, action: PayloadAction<IUser>) => {
      state.currentUser = action.payload;
    },
    addUserSubscriptions: (state, action: PayloadAction<ISubscription[]>) => {
      state.userSubscriptions = action.payload;
    },
    addPaymentMethods: (state, action: PayloadAction<IPaymentMethod[]>) => {
      state.paymentMethods = action.payload;
    },
    addPaymentHistory: (state, action: PayloadAction<IPayment[]>) => {
      state.paymentHistory = action.payload;
    },
  },
});

export const {
  addCurrentUser,
  addUserSubscriptions,
  addPaymentMethods,
  addPaymentHistory,
} = currentUserSlice.actions;
export const reducer = currentUserSlice.reducer;
