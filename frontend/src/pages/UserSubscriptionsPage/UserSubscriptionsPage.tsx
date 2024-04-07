import { ReactElement, useState } from 'react';
import { useSelectorTyped } from '../../hooks/store';
import { TabContext, TabList, TabPanel } from '@mui/lab';
import { Tab } from '@mui/material';
import styled from 'styled-components';
import UserCardList from '../../components/UserCardList/UserCardList';

const Title = styled.h1`
  margin: 0;
  padding-block: 12px 20px;
  font-weight: 600;
  font-size: 24px;
  line-height: 1.5;
  text-align: left;
  color: var(--black);
`;

const CategoryImg = styled.img`
  max-width: 20px;
`;

function UserSubscriptionsPage(): ReactElement {
  const [tabValue, setTabValue] = useState('0');

  //TODO переделать на подписки пользователя
  const userSubscriptions = useSelectorTyped(
    (store) => store.currentUserReducer.userSubscriptions
  );
  const categories = useSelectorTyped(
    (store) => store.servicesCategoriesReducer.servicesCategories
  );

  function handleTabChange(_event: React.SyntheticEvent, newValue: string) {
    setTabValue(newValue);
  }
  const tabs = () => {
    return categories.map((item, index) => (
      <Tab
        key={`category-tab-${index}`}
        label={<CategoryImg src={item.icon} alt={item.name} />}
        value={`${index + 1}`}
      />
    ));
  };

  return (
    <section>
      <Title>Мои подписки</Title>
      <TabContext value={tabValue}>
        <TabList
          onChange={handleTabChange}
          TabIndicatorProps={{
            sx: { display: 'none' },
          }}
        >
          <Tab label="Все" value="0" />
          {tabs()}
        </TabList>
        <TabPanel sx={{ p: 0 }} value="0">
          <UserCardList cardsList={userSubscriptions} />
        </TabPanel>
      </TabContext>
    </section>
  );
}

export default UserSubscriptionsPage;
