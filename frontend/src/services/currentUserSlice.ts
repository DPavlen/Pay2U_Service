import { IPaymentMethod, ISubscription, IUser } from '../utils/interfaces/interfaces.ts';
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface ICurrentUserState {
  currentUser: IUser;
  userSubscriptions: ISubscription[];
  paymentMethods: IPaymentMethod[]
}

const initialState: ICurrentUserState = {
  currentUser: {} as IUser,
  userSubscriptions: [],
  paymentMethods: []
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
  },
});

export const { addCurrentUser, addUserSubscriptions, addPaymentMethods } =
  currentUserSlice.actions;
export const reducer = currentUserSlice.reducer;
